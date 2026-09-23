from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.exceptions.user import UserAlreadyExistsError
from app.models.user import User
from app.services.user_service import UserService

router = APIRouter()

user_service = UserService()
@router.post("/")
def create_user(
    email:str,
    full_name: str,
    password:str,
    db:Session = Depends(get_db)
):
    user = User(
        email=email,
        hashed_password = password,
        full_name= full_name,
        role="engineer"
    )

    try:
        created_user = user_service.create_user(
            db,
            user,
        )
    except UserAlreadyExistsError:
        raise HTTPException(
            status_code=409,
            detail="A user with this email already exists."
        )

    return {
        "id":created_user.id,
        "email":created_user.email,
        "full_name":created_user.full_name,
        "role":created_user.role
    }