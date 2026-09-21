from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository


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
        return self.user_repository.create(
            db,
            user,
        )