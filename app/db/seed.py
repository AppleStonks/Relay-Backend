from datetime import datetime, timezone

from app.db.database import SessionLocal, Base, engine
from app.orm_models import Division, Team, Project, Person, Baton


def seed_db():
    db = SessionLocal()

    try:
        # Create tables if they do not already exist
        Base.metadata.create_all(bind=engine)

        # Division
        division = Division(name="Investment Banking")
        db.add(division)
        db.commit()
        db.refresh(division)

        # Team
        team = Team(name="Payment Platform", division_id=division.id)
        db.add(team)
        db.commit()
        db.refresh(team)

        # Projects
        project_1 = Project(name="Payment AWS Platform", team_id=team.id)
        project_2 = Project(name="Payments Legacy Migration", team_id=team.id)
        db.add_all([project_1, project_2])
        db.commit()
        db.refresh(project_1)
        db.refresh(project_2)

        # People
        software_engineer = Person(
            name="James Bond",
            username="bond",
            password="engineer123",
            role="software_engineer",
            team_id=team.id,
            in_office=True,
        )

        software_engineer_2 = Person(
            name="Julie Lee",
            username="lili",
            password="engineer123",
            role="software_engineer",
            team_id=team.id,
            in_office=True,
        )

        
        software_engineer_3 = Person(
            name="Dora Crum",
            username="dora",
            password="engineer123",
            role="software_engineer",
            team_id=team.id,
            in_office=False,
        )

        team_lead = Person(
            name="Amy Green",
            username="teamlead",
            password="teamlead123",
            role="team_lead",
            team_id=team.id,
            in_office=True,
        )

        resilience_manager = Person(
            name="Craig Wallis",
            username="resilience",
            password="resilience123",
            role="resilience_manager",
            team_id=team.id,
            in_office=True,
        )

        db.add_all([software_engineer, software_engineer_2, software_engineer_3, team_lead, resilience_manager])
        db.commit()
        db.refresh(software_engineer)
        db.refresh(team_lead)
        db.refresh(resilience_manager)

        # Batons
        baton_1 = Baton(
            project_id=project_1.id,
            owner_id=software_engineer.id,
            successor_ids=[software_engineer_2.id, team_lead.id],
            title="Add AWS Aurora DB for Payments Platform",
            description="Provisioning a high-availability Aurora PostgreSQL cluster for payment transaction persistence.",
            baton_status="in_progress",

            detailed_context=(
                "The cluster is being configured with a primary and one reader instance in 'eu-west-1'. "
                "We are using KMS for encryption at rest. Currently blocked on VPC peering request #992 "
                "to allow the payments-service to reach the new subnet."
            ),
            
            implementation_state="Development",
            repo_link="https://github.com/example/relay-core",
            branch_name="feature/payment-retry",
            
            daily_logs=[
                {
                    "date": "2026-04-05",
                    "note": "Implemented initial retry flow and basic tests.",
                },
                {
                    "date": "2026-04-06",
                    "note": "Configured Terraform scripts for RDS subnet groups and security groups.",

                }
            ],


            additional_resources=[
                {
                    "type": "confluence",
                    "title": "Payment Failure Scenarios",
                    "url": "https://confluence.example.com/x/payment-scenarios"
                },
                {
                    "type": "architecture_diagram",
                    "title": "Payments Cloud Infrastructure",
                    "url": "https://lucid.app/lucidchart/example-uuid"
                },
                {
                    "type": "runbook",
                    "title": "Aurora Migration Guide",
                    "url": "https://github.com/example/docs/runbooks/aurora-migration.md"
                }
            ],


            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )

        baton_2 = Baton(
            project_id=project_2.id,
            owner_id=software_engineer_3.id,
            successor_ids=[software_engineer_2.id, team_lead.id],
            title="Legacy Payment Gateway Decommissioning",
            description="Migrating the final 5% of traffic from the SOAP-based legacy gateway to the new REST API.",
            baton_status="awaiting_handover",
            
            detailed_context=(
                "All 'Standard' and 'Express' merchant types have been migrated. "
                "The remaining 5% consists of 'Enterprise' clients with custom header requirements. "
                "The adapter layer is written; we just need to flip the feature flag for the 'Acme Corp' test account."
            ),
            
            implementation_state="Ready for Migration",
            repo_link="https://github.com/example/legacy-bridge",
            branch_name="migration/enterprise-adapter-final",
            
            daily_logs=[
                {
                    "date": "2026-04-05",
                    "note": "Finalized the XML-to-JSON mapping for custom enterprise headers.",
                    "author": "Software Engineer"
                },
                {
                    "date": "2026-04-06",
                    "note": "Dry run successful in UAT environment. No regression detected in core flows.",
                    "author": "Software Engineer"
                }
            ],

            additional_resources=[
                {
                    "type": "spreadsheet",
                    "title": "Merchant Migration Tracker",
                    "url": "https://docs.google.com/spreadsheets/d/migration-status-123"
                },
                {
                    "type": "runbook",
                    "title": "Legacy Rollback Procedure",
                    "url": "https://github.com/example/docs/blob/main/rollback-legacy.md"
                },
                {
                    "type": "slack_thread",
                    "title": "Enterprise Client Approval Thread",
                    "url": "https://company.slack.com/archives/C123456/p162"
                }
            ],

            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )

        db.add_all([baton_1, baton_2])
        db.commit()

        print("Database seeded successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_db()