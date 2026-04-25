from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class DailyLogEntry(BaseModel):
    date: str
    note: str
    author: str | None = None


class BatonResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    # id
    id: int

    # timestamps
    created_at: datetime
    updated_at: datetime

    # ownership
    team_id: int | None = None

    project_id: int
    project_name: str | None = None

    owner_id: int
    owner_name: str | None = None

    successor_ids: list[int] | None = None

    # core baton info
    title: str
    description: str | None = None
    baton_status: str
    lifecycle_stage: str
    risk_label: str

    # handover / implementation details
    detailed_context: str | None = None
    implementation_state: str | None = None
    dependencies: str | None = None
    related_systems: str | None = None
    troubleshooting_notes: str | None = None
    reconstruction_time: int | None = None

    # links / resources
    repo_link: str | None = None
    branch_name: str | None = None
    additional_resources: list[dict[str, Any]] | None = None

    # progress tracking
    daily_logs: list[DailyLogEntry] | None = None


class BatonCreate(BaseModel):
    # required core creation fields
    project_id: int 
    owner_id: int
    title: str
    baton_status: str
    successor_ids: list[int] | None = None
    description: str | None = None

    # optional handover / implementation details
    detailed_context: str | None = None
    implementation_state: str | None = None
    dependencies: str | None = None
    related_systems: str | None = None
    troubleshooting_notes: str | None = None
    reconstruction_time: int | None = None

    # optional links / resources
    repo_link: str | None = None
    branch_name: str | None = None
    additional_resources: list[dict[str, Any]] | None = None


class BatonUpdate(BaseModel):
    # ownership / core editable fields
    owner_id: int | None = None
    successor_ids: list[int] | None = None
    title: str | None = None
    description: str | None = None
    baton_status: str | None = None

    # handover / implementation details
    detailed_context: str | None = None
    implementation_state: str | None = None
    dependencies: str | None = None
    related_systems: str | None = None
    troubleshooting_notes: str | None = None
    reconstruction_time: int | None = None

    # links / resources
    repo_link: str | None = None
    branch_name: str | None = None
    additional_resources: list[dict[str, Any]] | None = None

    # progress tracking
    daily_logs: list[DailyLogEntry] | None = None