from fastapi import Header, HTTPException, Depends
from typing import Optional
from src.config.settings import settings

def verify_admin(x_api_key: Optional[str] = Header(None)):
    """
    Very simple RBAC check for demo:
    - checks a static ADMIN_API_KEY header.
    Replace with real auth & permission checks.
    """
    if x_api_key != settings.ADMIN_API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden: admin credentials required")
    return True




from fastapi import Header, HTTPException, status, Depends

def admin_required(x_admin: str = Header(None)):
    """
    Simple RBAC stub:
    - Expect header X-Admin: "true" or an admin token.
    Replace with real auth + introspection in production.
    """
    if not x_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing admin credentials")
    if x_admin.lower() != "true":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin privileges required")
    # return admin identity stub (id)
    return {"admin_id": 101}
