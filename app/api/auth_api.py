from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.orm_models.person import Person
from app.pydantic_schemas.auth_schema import LoginRequest, LoginResponse

router = APIRouter()


@router.post("/auth/login", response_model=LoginResponse, tags=["Auth"])
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = (
        db.query(Person)
        .filter(
            Person.username == payload.username,
            Person.password == payload.password,
        )
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    return LoginResponse(
        user_id=user.id,
        name=user.name,
        role=user.role,
    )