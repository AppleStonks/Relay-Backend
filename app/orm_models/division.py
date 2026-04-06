from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.db.database import Base


class Division(Base):
    __tablename__ = "Division"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    
    name: Mapped[str] = mapped_column(String, nullable=False)