from sqlalchemy.orm import Session
from src.models.flagged_listings import FlaggedListing
from src.models.disputes import Dispute
from src.models.audit_logs import AuditLog
from src.common.events import publish_event
from src.common.exceptions import NotFoundError, ConflictError

def list_flagged(session: Session, status: str = None):
    q = session.query(FlaggedListing)
    if status:
        q = q.filter(FlaggedListing.status == status)
    return q.order_by(FlaggedListing.created_at.desc()).all()

def resolve_flag(session: Session, flag_id: int, resolved_by: int, notes: str = None):
    flag = session.query(FlaggedListing).filter(FlaggedListing.id == flag_id).first()
    if not flag:
        raise NotFoundError(detail=f"Flag id {flag_id} not found")
    if flag.status == "resolved":
        raise ConflictError(detail=f"Flag id {flag_id} already resolved")

    flag.status = "resolved"
    flag.resolved_at = func_now()
    flag.resolved_by = resolved_by
    session.add(flag)

    # Write audit log
    a = AuditLog(
        admin_id=resolved_by,
        action="resolve_flagged_listing",
        entity_type="flagged_listing",
        entity_id=flag_id,
        details={"notes": notes}
    )
    session.add(a)
    session.commit()

    publish_event("admin.action.logged", {
        "admin_id": resolved_by,
        "action": "resolve_flagged_listing",
        "entity_type": "flagged_listing",
        "entity_id": flag_id,
    })

    return flag

def resolve_dispute(session: Session, dispute_id: int, resolved_by: int, resolution_notes: str = None):
    dispute = session.query(Dispute).filter(Dispute.id == dispute_id).first()
    if not dispute:
        raise NotFoundError(detail=f"Dispute id {dispute_id} not found")
    if dispute.status == "resolved":
        raise ConflictError(detail=f"Dispute id {dispute_id} already resolved")

    dispute.status = "resolved"
    dispute.resolved_at = func_now()
    dispute.resolved_by = resolved_by
    dispute.resolution_notes = resolution_notes
    session.add(dispute)

    # audit log
    a = AuditLog(
        admin_id=resolved_by,
        action="resolve_dispute",
        entity_type="dispute",
        entity_id=dispute_id,
        details={"resolution_notes": resolution_notes}
    )
    session.add(a)
    session.commit()

    # publish event & (optionally) notifications
    publish_event("admin.action.logged", {
        "admin_id": resolved_by,
        "action": "resolve_dispute",
        "entity_type": "dispute",
        "entity_id": dispute_id,
        "resolution_notes": resolution_notes
    })

    # placeholder: notificationService.sendDisputeResolution(...)
    return dispute

# small helper to get current timestamp (SQL-friendly)
from datetime import datetime
def func_now():
    return datetime.utcnow()
