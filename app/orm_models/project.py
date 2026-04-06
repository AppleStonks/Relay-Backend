from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Project(Base):
    __tablename__ = "Project"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String, nullable=False)
    
    team_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("Team.id"),
        nullable=False,
    )