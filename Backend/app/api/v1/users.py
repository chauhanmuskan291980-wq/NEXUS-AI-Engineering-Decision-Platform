from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.exceptions.user import UserAlreadyExistsError
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService

router = APIRouter()

user_service = UserService()
@router.post("/",response_model=UserResponse)
def create_user(
    user_data : UserCreate,
    db:Session = Depends(get_db)
):

    try:
        created_user = user_service.create_user(
            db,
            user_data.email,
            user_data.full_name,
            user_data.password,
        )
    except UserAlreadyExistsError:
        raise HTTPException(
            status_code=409,
            detail="A user with this email already exists."
        )

    return created_user