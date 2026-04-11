from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.orm_models.baton import Baton
from app.orm_models.division import Division
from app.orm_models.person import Person
from app.orm_models.project import Project
from app.orm_models.team import Team
from app.pydantic_schemas.team_schema import TeamRiskResponse

router = APIRouter()


def calculate_delivery_delay_risk(score: int) -> str:
    if score >= 70:
        return "high"
    if score >= 40:
        return "medium"
    return "low"


@router.get("/teams/risk", response_model=list[TeamRiskResponse], tags=["Teams"])
def get_team_risk(
    team_id: int | None = Query(default=None),
    db: Session = Depends(get_db),
):
    query = db.query(Team)

    if team_id is not None:
        query = query.filter(Team.id == team_id)

    teams = query.all()

    results: list[TeamRiskResponse] = []

    for team in teams:
        division = db.query(Division).filter(Division.id == team.division_id).first()

        people = db.query(Person).filter(Person.team_id == team.id).all()
        total_staff = len(people)
        in_office_staff = sum(1 for person in people if person.in_office)

        if total_staff == 0:
            staff_availability_percentage = 0
        else:
            staff_availability_percentage = round((in_office_staff / total_staff) * 100)

        projects = db.query(Project).filter(Project.team_id == team.id).all()
        project_ids = [project.id for project in projects]

        if project_ids:
            batons = db.query(Baton).filter(Baton.project_id.in_(project_ids)).all()
        else:
            batons = []

        # "unassigned" here means at-risk / uncovered:
        # owner is out of office OR baton has no successors
        unassigned_baton_count = 0

        for baton in batons:
            owner = db.query(Person).filter(Person.id == baton.owner_id).first()
            owner_unavailable = owner is None or not owner.in_office
            no_successors = not baton.successor_ids

            if owner_unavailable or no_successors:
                unassigned_baton_count += 1

        # simple risk calculation
        availability_risk = 100 - staff_availability_percentage
        baton_risk = min(unassigned_baton_count * 20, 40)
        overall_risk_score = min(availability_risk + baton_risk, 100)

        delivery_delay_risk = calculate_delivery_delay_risk(overall_risk_score)

        results.append(
            TeamRiskResponse(
                team_id=team.id,
                team_name=team.name,
                division_id=team.division_id,
                division_name=division.name if division else "Unknown",
                staff_availability_percentage=staff_availability_percentage,
                unassigned_baton_count=unassigned_baton_count,
                delivery_delay_risk=delivery_delay_risk,
                overall_risk_score=overall_risk_score,
            )
        )

    return results