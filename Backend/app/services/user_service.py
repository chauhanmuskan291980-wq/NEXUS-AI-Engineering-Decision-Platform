from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.exceptions.user import UserAlreadyExistsError

class UserService:

    def __init__(self):
        self.user_repository = UserRepository()

    def get_user_by_email(
        self,
        db: Session,
        email: str,
    ) -> User | None:
        return self.user_repository.get_by_email(
            db,
            email,
        )

    def create_user(
    self,
    db: Session,
    user: User,
    ) -> User:
     existing_user = self.get_user_by_email(
        db,
        user.email,
    )

     if existing_user:
        raise UserAlreadyExistsError()

     return self.user_repository.create(
        db,
        user,
    )