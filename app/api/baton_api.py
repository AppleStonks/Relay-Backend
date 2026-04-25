from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.api.baton_status import normalize_baton_status
from app.orm_models.baton import Baton
from app.orm_models.person import Person
from app.orm_models.project import Project
from app.pydantic_schemas.baton_schema import BatonCreate, BatonResponse, BatonUpdate

router = APIRouter()

def determine_lifecycle_stage(baton: Baton) -> str:
    has_description = bool(baton.description and baton.description.strip())
    has_successors = bool(baton.successor_ids and len(baton.successor_ids) > 0)

    return "baton" if has_description and has_successors else "imported_ticket"


def calculate_baton_risk_label(baton: Baton) -> str:
    status = normalize_baton_status(baton.baton_status)
    if status == "done":
        return "Low Risk"
    if status in {"awaiting_handover", "handover_pending_approval"}:
        return "Critical Risk"
    if status == "enrich_ticket":
        return "High Risk"
    if status == "in_progress":
        has_successors = bool(baton.successor_ids and len(baton.successor_ids) > 0)
        has_description = bool(baton.description and baton.description.strip())
        if has_successors and has_description:
            return "Medium Risk"
        return "High Risk"
    return "Medium Risk"


def build_baton_response(db: Session, baton: Baton) -> BatonResponse:
    project = db.query(Project).filter(Project.id == baton.project_id).first()
    owner = db.query(Person).filter(Person.id == baton.owner_id).first()
    risk_label = calculate_baton_risk_label(baton)

    return BatonResponse(
        id=baton.id,
        created_at=baton.created_at,
        updated_at=baton.updated_at,

        team_id=project.team_id if project else None,

        project_id=baton.project_id,
        project_name=project.name if project else None,

        owner_id=baton.owner_id,
        owner_name=owner.name if owner else None,

        successor_ids=baton.successor_ids,
        title=baton.title,
        description=baton.description,
        detailed_context=baton.detailed_context,
        implementation_state=baton.implementation_state,
        repo_link=baton.repo_link,
        branch_name=baton.branch_name,
        daily_logs=baton.daily_logs,
        additional_resources=baton.additional_resources,
        baton_status=baton.baton_status,
        lifecycle_stage=baton.lifecycle_stage,
        risk_label=risk_label,

        dependencies=baton.dependencies,
        related_systems=baton.related_systems,
        troubleshooting_notes=baton.troubleshooting_notes,
        reconstruction_time=baton.reconstruction_time,
    )


@router.get("/batons", response_model=list[BatonResponse], tags=["Batons"])
def list_batons(
    owner_id: int | None = Query(default=None),
    project_id: int | None = Query(default=None),
    team_id: int | None = Query(default=None),
    db: Session = Depends(get_db),
):
    query = db.query(Baton)

    if owner_id is not None:
        query = query.filter(Baton.owner_id == owner_id)

    if project_id is not None:
        query = query.filter(Baton.project_id == project_id)

    if team_id is not None:
        query = query.join(Project, Baton.project_id == Project.id).filter(Project.team_id == team_id)

    batons = query.all()
    dirty = False
    for baton in batons:
        normalized_status = normalize_baton_status(baton.baton_status)
        if baton.baton_status != normalized_status:
            baton.baton_status = normalized_status
            dirty = True
    if dirty:
        db.commit()
        for baton in batons:
            db.refresh(baton)

    enriched_batons = []
    for baton in batons:
        enriched_batons.append(build_baton_response(db, baton))

    return enriched_batons


@router.get("/batons/{baton_id}", response_model=BatonResponse, tags=["Batons"])
def get_baton(baton_id: int, db: Session = Depends(get_db)):
    baton = db.query(Baton).filter(Baton.id == baton_id).first()

    if not baton:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Baton not found",
        )

    normalized_status = normalize_baton_status(baton.baton_status)
    if baton.baton_status != normalized_status:
        baton.baton_status = normalized_status
        db.commit()
        db.refresh(baton)

    return build_baton_response(db, baton)


@router.patch("/batons/{baton_id}", response_model=BatonResponse, tags=["Batons"])
def update_baton(baton_id: int, payload: BatonUpdate, db: Session = Depends(get_db)):
    baton = db.query(Baton).filter(Baton.id == baton_id).first()

    if not baton:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Baton not found",
        )

    previous_owner_id = baton.owner_id
    previous_owner = db.query(Person).filter(Person.id == previous_owner_id).first()
    previous_owner_name = previous_owner.name if previous_owner else f"User {previous_owner_id}"

    update_data = payload.model_dump(exclude_unset=True)
    if "baton_status" in update_data and update_data["baton_status"] is not None:
        update_data["baton_status"] = normalize_baton_status(update_data["baton_status"])

    if "daily_logs" in update_data and update_data["daily_logs"] is not None:
        normalized_logs = []
        for log in update_data["daily_logs"]:
            if hasattr(log, "model_dump"):
                normalized_logs.append(log.model_dump())
            elif isinstance(log, dict):
                normalized_logs.append(log)
        update_data["daily_logs"] = normalized_logs

    for field, value in update_data.items():
        setattr(baton, field, value)

    if "owner_id" in update_data and baton.owner_id != previous_owner_id:
        new_owner = db.query(Person).filter(Person.id == baton.owner_id).first()
        new_owner_name = new_owner.name if new_owner else f"User {baton.owner_id}"
        owner_change_entry = {
            "date": datetime.utcnow().date().isoformat(),
            "note": f"[OWNER_CHANGE] {previous_owner_name} -> {new_owner_name}",
        }
        existing_logs = list(baton.daily_logs or [])
        existing_logs.append(owner_change_entry)
        baton.daily_logs = existing_logs

    baton.lifecycle_stage = determine_lifecycle_stage(baton)

    db.commit()
    db.refresh(baton)

    return build_baton_response(db, baton)


@router.post("/batons", response_model=BatonResponse, tags=["Batons"], status_code=201)
def create_baton(payload: BatonCreate, db: Session = Depends(get_db)):
    baton = Baton(
        project_id=payload.project_id,
        owner_id=payload.owner_id,
        successor_ids=payload.successor_ids,
        title=payload.title,
        description=payload.description,
        detailed_context=payload.detailed_context,
        implementation_state=payload.implementation_state,
        repo_link=payload.repo_link,
        branch_name=payload.branch_name,
        additional_resources=payload.additional_resources or [],
        daily_logs=[],
        baton_status=normalize_baton_status(payload.baton_status),
        dependencies=payload.dependencies,
        related_systems=payload.related_systems,
        troubleshooting_notes=payload.troubleshooting_notes,
        reconstruction_time=payload.reconstruction_time,
        lifecycle_stage="imported_ticket",
    )

    baton.lifecycle_stage = determine_lifecycle_stage(baton)

    db.add(baton)
    db.commit()
    db.refresh(baton)

    return build_baton_response(db, baton)