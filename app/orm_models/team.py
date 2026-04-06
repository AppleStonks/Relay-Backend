from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Team(Base):
    __tablename__ = "Team"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    
    name: Mapped[str] = mapped_column(String, nullable=False)
    
    division_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("Division.id"),
        nullable=False,
    )