# SQLite DB

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./relay.db"

# engine knows how to talk to db (layer between sqlachemy and sqllite db)
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # needed for SQLite
)

# session is work context for db operation
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# parent class to be inherited to SQLAlchemy knows what classes are used for ORM
Base = declarative_base()

# helper  function to get a db session
# gives the db session but then comes back to close db session after - clean up
def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()