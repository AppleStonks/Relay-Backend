from pydantic import BaseModel, ConfigDict


class PersonResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    username: str
    role: str
    team_id: int
    in_office: bool


class PersonUpdate(BaseModel):
    in_office: bool