from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, JSON, String, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Baton(Base):
    __tablename__ = "Baton"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    project_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("Project.id"),
        nullable=False,
        index=True,
    )
    
    owner_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("Person.id"),
        nullable=False,
        index=True,
    )

    successor_ids: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True,
        default=list,
    )

    title: Mapped[str] = mapped_column(String, nullable=False)

    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    
    detailed_context: Mapped[str | None] = mapped_column(Text, nullable=True)

    implementation_state: Mapped[str | None] = mapped_column(Text, nullable=True)

    repo_link: Mapped[str | None] = mapped_column(String, nullable=True)

    branch_name: Mapped[str | None] = mapped_column(String, nullable=True)

    daily_logs: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True,
        default=list,
    )

    additional_resources: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True,
        default=list,
    )

    baton_status: Mapped[str] = mapped_column(Boolean, nullable=False)