from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

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

    return {
        "message": "User lookup completed",
        "user_found": user is not None,
    }