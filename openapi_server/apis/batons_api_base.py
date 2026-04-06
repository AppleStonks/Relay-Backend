# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictInt
from typing import List, Optional
from typing_extensions import Annotated
from openapi_server.models.baton import Baton
from openapi_server.models.baton_update import BatonUpdate
from openapi_server.models.error import Error


class BaseBatonsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseBatonsApi.subclasses = BaseBatonsApi.subclasses + (cls,)
    async def list_batons(
        self,
        owner_id: Annotated[Optional[StrictInt], Field(description="Filter batons by current owner")],
        project_id: Annotated[Optional[StrictInt], Field(description="Filter batons by project")],
        team_id: Annotated[Optional[StrictInt], Field(description="Filter batons by team")],
    ) -> List[Baton]:
        ...


    async def get_baton(
        self,
        batonId: StrictInt,
    ) -> Baton:
        ...


    async def update_baton(
        self,
        batonId: StrictInt,
        baton_update: BatonUpdate,
    ) -> Baton:
        ...
