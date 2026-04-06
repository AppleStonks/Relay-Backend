from fastapi import FastAPI
from app.db.database import Base, engine
from openapi_server.apis.auth_api import router as auth_router

app = FastAPI(
    title="Relay API",
    version="1.0.0",
    description="Relay backend API"
)

app.include_router(auth_router)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Relay API is running"}