from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Person(Base):
    __tablename__ = "Person"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String, nullable=False)

    username: Mapped[str] = mapped_column(String, nullable=False, unique=True, index=True) # index = True for faster queries

    password: Mapped[str] = mapped_column(String, nullable=False)

    role: Mapped[str] = mapped_column(String, nullable=False)

    team_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("Team.id"),
        nullable=False,
    )
    
    in_office: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)