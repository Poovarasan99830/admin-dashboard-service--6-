from fastapi import Header, Depends
from src.common.exceptions import Forbidden, Unauthorized
from typing import Optional

def verify_admin(x_admin_role: Optional[str] = Header(None), x_admin_id: Optional[str] = Header(None)):
    """
    Simple RBAC dependency for dev:
    - expects header `x-admin-role: admin` and `x-admin-id: <id>`
    In production this would validate JWT and check claims/permissions.
    """
    if x_admin_id is None:
        raise Unauthorized("Missing admin id")
    if x_admin_role != "admin":
        raise Forbidden("Admin role required")
    # return admin identity for logging
    return {"admin_id": int(x_admin_id)}
