from sqlalchemy.orm import Session
from sqlalchemy import func
from src.models.audit_logs import AuditLog


def get_analytics(db: Session):
    """Aggregate disputes, flags, and total logs."""
    disputes_resolved = db.query(AuditLog).filter(AuditLog.action == "dispute_resolved").count()
    flags_handled = db.query(AuditLog).filter(AuditLog.action == "flag_handled").count()
    total_logs = db.query(func.count(AuditLog.id)).scalar()
    return {
        "disputes_resolved": disputes_resolved,
        "flags_handled": flags_handled,
        "total_logs": total_logs,
    }


def get_audit_logs(db: Session, skip: int = 0, limit: int = 50):
    """Fetch paginated audit logs."""
    return db.query(AuditLog).order_by(AuditLog.created_at.desc()).offset(skip).limit(limit).all()
