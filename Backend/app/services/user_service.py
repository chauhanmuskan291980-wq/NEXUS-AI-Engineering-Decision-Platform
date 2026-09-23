from sqlalchemy.orm import Session
from app.core.security import hash_password
from app.exceptions.user import UserAlreadyExistsError
from app.models.user import User
from app.repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_user_by_email(
            self,
            db:Session,
            email:str,
    ) -> User | None :
        return self.user_repository.get_by_email(
            db,
            email
        )

    def create_user(
            self,
            db:Session,
            email:str,
            full_name:str,
            password:str
    )-> User:
        existing_user = self.get_user_by_email(
            db,
            email
        )

        if existing_user:
            raise UserAlreadyExistsError

        hashed_password = hash_password(password)
        user = User(
            email=email,
            hashed_password=hashed_password,
            full_name=full_name,
            role="engineer",
        )

        return self.user_repository.create(
            db,
            user
        )