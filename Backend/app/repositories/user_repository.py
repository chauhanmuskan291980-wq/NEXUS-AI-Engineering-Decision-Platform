from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    def get_by_email(
        self,
        db: Session,
        email: str,
    ) -> User | None:
        statement = select(User).where(User.email == email)

        return db.execute(statement).scalar_one_or_none()

    def create(
        self,
        db: Session,
        user: User,
    ) -> User:
        db.add(user)
        db.commit()
        db.refresh(user)

        return user
# scalar_one_or_none ----> One Matching user ---> Return that user , no matching user ---> Return Noen , Multiple matching users --- raise an error 
