from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class DailyLogEntry(BaseModel):
    date: str
    note: str


class BatonResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
    project_id: int
    owner_id: int
    successor_ids: list[int] | None = None
    title: str
    description: str | None = None
    detailed_context: str | None = None
    implementation_state: str | None = None
    repo_link: str | None = None
    branch_name: str | None = None
    daily_logs: list[DailyLogEntry] | None = None
    additional_resources: list[dict[str, Any]] | None = None
    baton_status: str


class BatonCreate(BaseModel):
    project_id: int
    owner_id: int
    title: str
    baton_status: str
    successor_ids: list[int]
    description: str

    detailed_context: str | None = None
    implementation_state: str | None = None
    repo_link: str | None = None
    branch_name: str | None = None
    additional_resources: list[dict[str, Any]] | None = None

class BatonUpdate(BaseModel):
    successor_ids: list[int] | None = None
    title: str | None = None
    description: str | None = None
    detailed_context: str | None = None
    implementation_state: str | None = None
    repo_link: str | None = None
    branch_name: str | None = None
    daily_logs: list[DailyLogEntry] | None = None
    additional_resources: list[dict[str, Any]] | None = None
    baton_status: str | None = None