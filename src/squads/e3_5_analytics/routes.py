from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.common.database import get_db
from src.squads.e3_5_analytics import schema, service

router = APIRouter(prefix="/api/v1/admin", tags=["analytics"])


@router.get("/analytics", response_model=schema.AnalyticsResponse)
def analytics(db: Session = Depends(get_db)):
    data = service.get_analytics(db)
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No analytics available")
    return data


@router.get("/audit-logs", response_model=list[schema.AuditLogResponse])
def audit_logs(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    logs = service.get_audit_logs(db, skip, limit)
    if not logs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No logs found")
    return logs
