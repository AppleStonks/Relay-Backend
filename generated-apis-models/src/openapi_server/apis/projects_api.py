# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.projects_api_base import BaseProjectsApi
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
from openapi_server.models.error import Error
from openapi_server.models.project import Project


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/projects",
    responses={
        200: {"model": List[Project], "description": "List of matching projects"},
    },
    tags=["Projects"],
    summary="Get projects, optionally filtered by person or team",
    response_model_by_alias=True,
)
async def list_projects(
    person_id: Annotated[Optional[StrictInt], Field(description="Filter projects associated with a specific person")] = Query(None, description="Filter projects associated with a specific person", alias="person_id"),
    team_id: Annotated[Optional[StrictInt], Field(description="Filter projects belonging to a specific team")] = Query(None, description="Filter projects belonging to a specific team", alias="team_id"),
) -> List[Project]:
    if not BaseProjectsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseProjectsApi.subclasses[0]().list_projects(person_id, team_id)


@router.get(
    "/projects/{projectId}",
    responses={
        200: {"model": Project, "description": "Project found"},
        404: {"model": Error, "description": "Project not found"},
    },
    tags=["Projects"],
    summary="Get a specific project by ID",
    response_model_by_alias=True,
)
async def get_project(
    projectId: StrictInt = Path(..., description=""),
) -> Project:
    if not BaseProjectsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseProjectsApi.subclasses[0]().get_project(projectId)
