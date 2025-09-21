from fastapi import APIRouter, Depends, HTTPException
from typing import List
from src.common.rbac import verify_admin
from src.common.database import get_session
from src.squads.e3_2_marketplace import service, schema
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/flagged", response_model=List[schema.FlaggedListingOut], dependencies=[Depends(verify_admin)])
def get_flagged(status: str = None, db: Session = Depends(get_session)):
    rows = service.list_flagged(db, status)
    return rows

@router.post("/flagged/{id}/resolve", response_model=schema.ResolveFlagOut, dependencies=[Depends(verify_admin)])
def post_resolve_flag(id: int, payload: schema.ResolveFlagIn, db: Session = Depends(get_session)):
    try:
        flag = service.resolve_flag(db, id, payload.resolved_by, payload.notes)
        return flag
    except HTTPException as exc:
        raise exc

@router.post("/disputes/{id}/resolve", response_model=schema.ResolveDisputeOut, dependencies=[Depends(verify_admin)])
def post_resolve_dispute(id: int, payload: schema.ResolveDisputeIn, db: Session = Depends(get_session)):
    try:
        dispute = service.resolve_dispute(db, id, payload.resolved_by, payload.resolution_notes)
        # In real app: notificationService.sendDisputeResolution(dispute)
        return dispute
    except HTTPException as exc:
        raise exc
