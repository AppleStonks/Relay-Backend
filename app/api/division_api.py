from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.orm_models.baton import Baton
from app.orm_models.division import Division
from app.orm_models.person import Person
from app.orm_models.project import Project
from app.orm_models.team import Team
from app.pydantic_schemas.division_schema import DivisionRiskResponse

router = APIRouter()


@router.get("/division/risk", response_model=list[DivisionRiskResponse], tags=["Divisions"])
def get_division_risk(
    division_id: int | None = Query(default=None),
    db: Session = Depends(get_db),
):
    query = db.query(Division)

    if division_id is not None:
        query = query.filter(Division.id == division_id)

    divisions = query.all()

    results: list[DivisionRiskResponse] = []

    for division in divisions:
        teams = db.query(Team).filter(Team.division_id == division.id).all()
        team_ids = [team.id for team in teams]

        if team_ids:
            people = db.query(Person).filter(Person.team_id.in_(team_ids)).all()
            projects = db.query(Project).filter(Project.team_id.in_(team_ids)).all()
        else:
            people = []
            projects = []

        total_staff = len(people)
        in_office_staff = sum(1 for person in people if person.in_office)

        if total_staff == 0:
            staff_availability_percentage = 0
        else:
            staff_availability_percentage = round((in_office_staff / total_staff) * 100)

        project_ids = [project.id for project in projects]

        if project_ids:
            batons = db.query(Baton).filter(Baton.project_id.in_(project_ids)).all()
        else:
            batons = []

        batons_ready_for_handover = sum(
            1 for baton in batons if baton.baton_status == "awaiting_handover"
        )

        batons_unassigned = 0
        for baton in batons:
            owner = db.query(Person).filter(Person.id == baton.owner_id).first()
            owner_unavailable = owner is None or not owner.in_office
            no_successors = not baton.successor_ids

            if owner_unavailable or no_successors:
                batons_unassigned += 1

        availability_risk = 100 - staff_availability_percentage
        handover_risk = min(batons_ready_for_handover * 10, 30)
        unassigned_risk = min(batons_unassigned * 20, 40)

        overall_risk_score = min(availability_risk + handover_risk + unassigned_risk, 100)

        results.append(
            DivisionRiskResponse(
                division_id=division.id,
                division_name=division.name,
                staff_availability_percentage=staff_availability_percentage,
                batons_ready_for_handover=batons_ready_for_handover,
                batons_unassigned=batons_unassigned,
                overall_risk_score=overall_risk_score,
            )
        )

    return results