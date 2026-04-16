from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.orm_models.person import Person
from app.pydantic_schemas.person_schema import PersonResponse, PersonUpdate

router = APIRouter()


@router.get("/person/{person_id}", response_model=PersonResponse, tags=["Persons"])
def get_person(person_id: int, db: Session = Depends(get_db)):
    person = db.query(Person).filter(Person.id == person_id).first()

    if not person:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Person not found",
        )

    return person


@router.patch("/person/{person_id}", response_model=PersonResponse, tags=["Persons"])
def update_person(person_id: int, payload: PersonUpdate, db: Session = Depends(get_db)):
    person = db.query(Person).filter(Person.id == person_id).first()

    if not person:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Person not found",
        )

    person.in_office = payload.in_office

    db.commit()
    db.refresh(person)

    return person