from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class AnalyticsResponse(BaseModel):
    disputes_resolved: int
    flags_handled: int
    total_logs: int


class AuditLogResponse(BaseModel):
    id: UUID
    action: str
    user_id: UUID
    target_id: UUID | None
    created_at: datetime

    class Config:
        orm_mode = True
