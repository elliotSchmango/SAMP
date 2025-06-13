from fastapi import Depends, HTTPException
from models import User
from auth import get_current_user


def require_role(required_role: str):
    def role_checker(user: User = Depends(get_current_user)):
        if user.role != required_role:
            raise HTTPException(status_code=403, detail="Forbidden: Insufficient role")
        return user
    return role_checker