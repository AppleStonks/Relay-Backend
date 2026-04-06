# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.batons_api_base import BaseBatonsApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from pydantic import Field, StrictInt
from typing import List, Optional
from typing_extensions import Annotated
from openapi_server.models.baton import Baton
from openapi_server.models.baton_update import BatonUpdate
from openapi_server.models.error import Error


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/batons",
    responses={
        200: {"model": List[Baton], "description": "List of matching batons"},
    },
    tags=["Batons"],
    summary="Get batons, optionally filtered by owner, project, or team",
    response_model_by_alias=True,
)
async def list_batons(
    owner_id: Annotated[Optional[StrictInt], Field(description="Filter batons by current owner")] = Query(None, description="Filter batons by current owner", alias="owner_id"),
    project_id: Annotated[Optional[StrictInt], Field(description="Filter batons by project")] = Query(None, description="Filter batons by project", alias="project_id"),
    team_id: Annotated[Optional[StrictInt], Field(description="Filter batons by team")] = Query(None, description="Filter batons by team", alias="team_id"),
) -> List[Baton]:
    if not BaseBatonsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseBatonsApi.subclasses[0]().list_batons(owner_id, project_id, team_id)


@router.get(
    "/batons/{batonId}",
    responses={
        200: {"model": Baton, "description": "Baton found"},
        404: {"model": Error, "description": "Baton not found"},
    },
    tags=["Batons"],
    summary="Get a specific baton by ID",
    response_model_by_alias=True,
)
async def get_baton(
    batonId: StrictInt = Path(..., description=""),
) -> Baton:
    if not BaseBatonsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseBatonsApi.subclasses[0]().get_baton(batonId)


@router.patch(
    "/batons/{batonId}",
    responses={
        200: {"model": Baton, "description": "Baton updated successfully"},
        404: {"model": Error, "description": "Baton not found"},
    },
    tags=["Batons"],
    summary="Update editable fields of a baton",
    response_model_by_alias=True,
)
async def update_baton(
    batonId: StrictInt = Path(..., description=""),
    baton_update: BatonUpdate = Body(None, description=""),
) -> Baton:
    if not BaseBatonsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseBatonsApi.subclasses[0]().update_baton(batonId, baton_update)
