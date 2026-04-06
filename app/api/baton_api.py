from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.orm_models.baton import Baton
from app.orm_models.project import Project
from app.pydantic_schemas.baton_schema import BatonResponse, BatonUpdate, BatonCreate

router = APIRouter()


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

    elif project_id is not None:
        query = query.filter(Baton.project_id == project_id)

    elif team_id is not None:
        query = query.join(Project, Baton.project_id == Project.id).filter(Project.team_id == team_id)

    batons = query.all()

    return batons


@router.get("/batons/{baton_id}", response_model=BatonResponse, tags=["Batons"])
def get_baton(baton_id: int, db: Session = Depends(get_db)):
    baton = db.query(Baton).filter(Baton.id == baton_id).first()

    if not baton:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Baton not found",
        )

    return baton


# endpoint to update baton - only updates fields that were set
@router.patch("/batons/{baton_id}", response_model=BatonResponse, tags=["Batons"])
def update_baton(baton_id: int, payload: BatonUpdate, db: Session = Depends(get_db)):
    baton = db.query(Baton).filter(Baton.id == baton_id).first()

    if not baton:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Baton not found",
        )

    update_data = payload.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(baton, field, value)

    db.commit()
    db.refresh(baton)

    return baton


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
        baton_status=payload.baton_status,
    )

    db.add(baton)
    db.commit()
    db.refresh(baton)

    return baton