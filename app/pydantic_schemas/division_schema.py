from pydantic import BaseModel


class DivisionRiskResponse(BaseModel):
    division_id: int
    division_name: str

    staff_availability_percentage: int
    batons_ready_for_handover: int
    batons_unassigned: int

    overall_risk_score: int