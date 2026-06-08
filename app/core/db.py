from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.config import settings


def get_session() -> Session:
    engine = create_engine(settings.database_url, pool_pre_ping=True)
    return sessionmaker(bind=engine)(autocommit=False, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
