from sqlalchemy.orm import Session
from src.models.providers import Provider, ProviderStatus
from src.models.admin_actions import AdminAction, AdminActionType
from src.common.events import emit_admin_action_logged
from datetime import datetime

def suspend_provider(db: Session, provider_id: int, admin_id: int, reason: str):
    provider = db.query(Provider).filter(Provider.id == provider_id).one_or_none()
    if not provider:
        return None, "not_found"
    # idempotent: if already suspended, still return current state
    if provider.status != ProviderStatus.suspended:
        provider.status = ProviderStatus.suspended
        provider.updated_at = datetime.utcnow()
        db.add(provider)
        db.flush()
    # log action (immutable)
    action = AdminAction(admin_id=admin_id, provider_id=provider_id, action=AdminActionType.suspend, reason=reason)
    db.add(action)
    db.commit()
    emit_admin_action_logged({"admin_id": admin_id, "provider_id": provider_id, "action": "suspend", "reason": reason})
    return provider, None

def restore_provider(db: Session, provider_id: int, admin_id: int, reason: str):
    provider = db.query(Provider).filter(Provider.id == provider_id).one_or_none()
    if not provider:
        return None, "not_found"
    if provider.status != ProviderStatus.active:
        provider.status = ProviderStatus.active
        provider.updated_at = datetime.utcnow()
        db.add(provider)
        db.flush()
    action = AdminAction(admin_id=admin_id, provider_id=provider_id, action=AdminActionType.restore, reason=reason)
    db.add(action)
    db.commit()
    emit_admin_action_logged({"admin_id": admin_id, "provider_id": provider_id, "action": "restore", "reason": reason})
    return provider, None

def get_flagged_bookings(db: Session, status: str = None, date_from=None, date_to=None):
    from src.models.flagged_bookings import FlaggedBooking
    q = db.query(FlaggedBooking)
    if status:
        q = q.filter(FlaggedBooking.status == status)
    if date_from:
        q = q.filter(FlaggedBooking.created_at >= date_from)
    if date_to:
        q = q.filter(FlaggedBooking.created_at <= date_to)
    return q.order_by(FlaggedBooking.created_at.desc()).all()
