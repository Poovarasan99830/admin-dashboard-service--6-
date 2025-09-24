from fastapi import APIRouter, Depends, Query, Path, Body
from typing import Optional
from src.common.database import get_session
from sqlalchemy.orm import Session
from src.squads.e3_1_user_mgmt import service, schema
from src.common.rbac import verify_admin

router = APIRouter()

@router.get("", response_model=schema.UsersListResponse)
def get_users(
    name: Optional[str] = Query(None),
    email: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    limit: int = Query(25, ge=1, le=500),
    db: Session = Depends(get_session),
    admin=Depends(verify_admin),
):
    users, meta = service.list_users(db, name=name, email=email, status=status, page=page, limit=limit)
    return {"users": users, "meta": meta}




@router.post("/{user_id}/suspend", response_model=schema.ActionResponse)
def suspend_user(
    user_id: int = Path(..., ge=1),
    payload: schema.SuspendRestoreRequest = Body(...),
    db: Session = Depends(get_session),
    admin=Depends(verify_admin),
):
    admin_id = admin["admin_id"]
    user = service.suspend_user(db, user_id=user_id, admin_id=admin_id, reason=payload.reason)
    return {"message": "User suspended successfully", "user": user}






@router.post("/{user_id}/restore", response_model=schema.ActionResponse)
def restore_user(
    user_id: int = Path(..., ge=1),
    payload: schema.SuspendRestoreRequest = Body(...),
    db: Session = Depends(get_session),
    admin=Depends(verify_admin),
):
    admin_id = admin["admin_id"]
    user = service.restore_user(db, user_id=user_id, admin_id=admin_id, reason=payload.reason)
    return {"message": "User restored successfully", "user": user}
