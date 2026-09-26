from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.core.security import verify_password
from app.db.dependencies import get_db
from app.schemas.auth import LoginRequest
from app.services.user_service import UserService


router = APIRouter()

user_service = UserService()


@router.post("/login")
def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db),
):
    user = user_service.get_user_by_email(
        db,
        login_data.email,
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    password_valid = verify_password(
        login_data.password,
        user.hashed_password
    )

    if not password_valid:
        raise HTTPException(
            status_code=401,
            detail="Invaild email or password"
        )

    return {
        "message": "User lookup completed",
        "user_found": user.id,
        "email":user.email
    }