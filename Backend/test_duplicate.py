from app.db.session import SessionLocal
from app.models.user import User
from app.services.user_service import UserService
from app.exceptions.user import UserAlreadyExistsError


db = SessionLocal()

try:
    user = User(
        email="duplicate-test@example.com",
        hashed_password="dummy-hash",
        full_name="Another User",
        role="engineer",
    )

    service = UserService()

    service.create_user(
        db,
        user,
    )

    print("ERROR: duplicate user was created")

except UserAlreadyExistsError:
    print("SUCCESS: duplicate email rejected")

finally:
    db.close()