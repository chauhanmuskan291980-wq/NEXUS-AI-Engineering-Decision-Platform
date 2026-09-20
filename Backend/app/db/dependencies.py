from collections.abc import Generator
from sqlalchemy.orm import Session
from app.db.session import sessionLocal

def get_db()->Generator[Session,None,None]:
    db = sessionLocal()  ## creates a SQLAlchemy session.

    try:
        yield db   ## gives that session to the FastAPI endpoint.
    finally:
        db.close()   ## runs when the request is finished