from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FlaggedListingOut(BaseModel):
    id: int
    listing_id: int
    reason: str
    status: str
    created_at: datetime
    resolved_at: Optional[datetime] = None
    resolved_by: Optional[int] = None

    class Config:
        orm_mode = True

class ResolveFlagIn(BaseModel):
    resolved_by: int
    notes: Optional[str] = None

class ResolveFlagOut(BaseModel):
    id: int
    status: str
    resolved_at: Optional[datetime]
    resolved_by: Optional[int]

    class Config:
        orm_mode = True

class DisputeOut(BaseModel):
    id: int
    user_id: int
    listing_id: int
    status: str
    created_at: datetime
    resolved_at: Optional[datetime]
    resolved_by: Optional[int]
    resolution_notes: Optional[str]

    class Config:
        orm_mode = True

class ResolveDisputeIn(BaseModel):
    resolved_by: int
    resolution_notes: Optional[str] = None

class ResolveDisputeOut(BaseModel):
    id: int
    status: str
    resolved_at: Optional[datetime]
    resolved_by: Optional[int]

    class Config:
        orm_mode = True
