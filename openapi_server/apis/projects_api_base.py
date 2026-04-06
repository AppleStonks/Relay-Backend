# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictInt
from typing import List, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.project import Project


class BaseProjectsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseProjectsApi.subclasses = BaseProjectsApi.subclasses + (cls,)
    async def list_projects(
        self,
        person_id: Annotated[Optional[StrictInt], Field(description="Filter projects associated with a specific person")],
        team_id: Annotated[Optional[StrictInt], Field(description="Filter projects belonging to a specific team")],
    ) -> List[Project]:
        ...


    async def get_project(
        self,
        projectId: StrictInt,
    ) -> Project:
        ...
