from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.auth_api import router as auth_router
from app.api.baton_api import router as baton_router
from app.api.team_api import router as team_router
from app.api.division_api import router as division_router
from app.api.person_api import router as person_router

app = FastAPI(
    title="Relay API",
    version="1.0.0",
    description="Relay backend API"
)

app.include_router(auth_router)
app.include_router(baton_router)
app.include_router(team_router)
app.include_router(division_router)
app.include_router(person_router)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Relay API is running"}