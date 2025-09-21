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
