from datetime import datetime, timezone

from app.db.database import SessionLocal, Base, engine
from app.orm_models import Division, Team, Project, Person, Baton


def seed_db():
    db = SessionLocal()

    try:
        # Drop all tables if they exist
        Base.metadata.drop_all(bind=engine)

        # Create tables if they do not already exist
        Base.metadata.create_all(bind=engine)

        # Divisions
        investment_banking = Division(name="Investment Banking")
        core_engineering = Division(name="Core Engineering")
        db.add_all([investment_banking, core_engineering])
        db.commit()
        db.refresh(investment_banking)
        db.refresh(core_engineering)

        # Teams
        payment_platform_team = Team(name="Payment Platform", division_id=investment_banking.id)
        trading_systems_team = Team(name="Trading Systems", division_id=investment_banking.id)
        infrastructure_team = Team(name="Infrastructure Team", division_id=core_engineering.id)
        db.add_all([payment_platform_team, trading_systems_team, infrastructure_team])
        db.commit()
        db.refresh(payment_platform_team)
        db.refresh(trading_systems_team)
        db.refresh(infrastructure_team)

        # Projects for Payment Platform Team
        payment_aws_project = Project(name="Payment AWS Platform", team_id=payment_platform_team.id)
        payments_legacy_migration = Project(name="Payments Legacy Migration", team_id=payment_platform_team.id)
        db.add_all([payment_aws_project, payments_legacy_migration])
        db.commit()
        db.refresh(payment_aws_project)
        db.refresh(payments_legacy_migration)

        # Projects for Trading Systems Team
        algorithmic_trading_project = Project(name="Algorithmic Trading Engine", team_id=trading_systems_team.id)
        risk_management_project = Project(name="Real-time Risk Management", team_id=trading_systems_team.id)
        db.add_all([algorithmic_trading_project, risk_management_project])
        db.commit()
        db.refresh(algorithmic_trading_project)
        db.refresh(risk_management_project)

        # Projects for Infrastructure Team
        cloud_infrastructure_project = Project(name="Cloud Infrastructure Automation", team_id=infrastructure_team.id)
        monitoring_systems_project = Project(name="Enterprise Monitoring Systems", team_id=infrastructure_team.id)
        db.add_all([cloud_infrastructure_project, monitoring_systems_project])
        db.commit()
        db.refresh(cloud_infrastructure_project)
        db.refresh(monitoring_systems_project)

        # People for Payment Platform Team
        payment_engineer_1 = Person(
            name="James Bond",
            username="bond",
            password="engineer123",
            role="software_engineer",
            team_id=payment_platform_team.id,
            in_office=True,
        )

        payment_engineer_2 = Person(
            name="Andrew Mullins",
            username="drew",
            password="engineer123",
            role="software_engineer",
            team_id=payment_platform_team.id,
            in_office=True,
        )

        payment_engineer_3 = Person(
            name="Dora Crum",
            username="dora",
            password="engineer123",
            role="software_engineer",
            team_id=payment_platform_team.id,
            in_office=False,
        )

        payment_engineer_4 = Person(
            name="Sarah Chen",
            username="schen",
            password="engineer123",
            role="software_engineer",
            team_id=payment_platform_team.id,
            in_office=True,
        )

        payment_team_lead = Person(
            name="Amy Green",
            username="teamlead",
            password="teamlead123",
            role="team_lead",
            team_id=payment_platform_team.id,
            in_office=True,
        )

        payment_resilience_manager = Person(
            name="Craig Wallis",
            username="resilience",
            password="resilience123",
            role="resilience_manager",
            team_id=payment_platform_team.id,
            in_office=True,
        )

        # People for Trading Systems Team
        trading_engineer_1 = Person(
            name="Michael Torres",
            username="mtorres",
            password="engineer123",
            role="software_engineer",
            team_id=trading_systems_team.id,
            in_office=True,
        )

        trading_engineer_2 = Person(
            name="Lisa Wong",
            username="lwong",
            password="engineer123",
            role="software_engineer",
            team_id=trading_systems_team.id,
            in_office=False,
        )

        trading_engineer_3 = Person(
            name="David Kim",
            username="dkim",
            password="engineer123",
            role="software_engineer",
            team_id=trading_systems_team.id,
            in_office=True,
        )

        trading_engineer_4 = Person(
            name="Emma Rodriguez",
            username="erod",
            password="engineer123",
            role="software_engineer",
            team_id=trading_systems_team.id,
            in_office=False,
        )

        trading_team_lead = Person(
            name="Robert Johnson",
            username="rjohnson",
            password="teamlead123",
            role="team_lead",
            team_id=trading_systems_team.id,
            in_office=True,
        )

        # People for Infrastructure Team
        infra_engineer_1 = Person(
            name="Jennifer Liu",
            username="jliu",
            password="engineer123",
            role="software_engineer",
            team_id=infrastructure_team.id,
            in_office=True,
        )

        infra_engineer_2 = Person(
            name="Alex Thompson",
            username="athompson",
            password="engineer123",
            role="software_engineer",
            team_id=infrastructure_team.id,
            in_office=True,
        )

        infra_engineer_3 = Person(
            name="Maria Garcia",
            username="mgarcia",
            password="engineer123",
            role="software_engineer",
            team_id=infrastructure_team.id,
            in_office=False,
        )

        infra_engineer_4 = Person(
            name="Kevin Patel",
            username="kpatel",
            password="engineer123",
            role="software_engineer",
            team_id=infrastructure_team.id,
            in_office=True,
        )

        infra_team_lead = Person(
            name="Sophia Anderson",
            username="sanderson",
            password="teamlead123",
            role="team_lead",
            team_id=infrastructure_team.id,
            in_office=True,
        )

        db.add_all([
            payment_engineer_1, payment_engineer_2, payment_engineer_3, payment_engineer_4,
            payment_team_lead, payment_resilience_manager,
            trading_engineer_1, trading_engineer_2, trading_engineer_3, trading_engineer_4,
            trading_team_lead,
            infra_engineer_1, infra_engineer_2, infra_engineer_3, infra_engineer_4,
            infra_team_lead,
        ])
        db.commit()
        # Refresh all people
        db.refresh(payment_engineer_1)
        db.refresh(payment_engineer_2)
        db.refresh(payment_engineer_3)
        db.refresh(payment_engineer_4)
        db.refresh(payment_team_lead)
        db.refresh(payment_resilience_manager)
        db.refresh(trading_engineer_1)
        db.refresh(trading_engineer_2)
        db.refresh(trading_engineer_3)
        db.refresh(trading_engineer_4)
        db.refresh(trading_team_lead)
        db.refresh(infra_engineer_1)
        db.refresh(infra_engineer_2)
        db.refresh(infra_engineer_3)
        db.refresh(infra_engineer_4)
        db.refresh(infra_team_lead)

        # Batons for Payment AWS Platform
        payment_aws_baton = Baton(
            project_id=payment_aws_project.id,
            owner_id=payment_engineer_1.id,
            successor_ids=[payment_engineer_2.id, payment_team_lead.id],
            title="Add AWS Aurora DB for Payments Platform",
            description="Provisioning a high-availability Aurora PostgreSQL cluster for payment transaction persistence.",
            baton_status="in_progress",
            detailed_context=(
                "The cluster is being configured with a primary and one reader instance in 'eu-west-1'. "
                "We are using KMS for encryption at rest. Currently blocked on VPC peering request #992 "
                "to allow the payments-service to reach the new subnet."
            ),
            implementation_state="Development",
            dependencies="VPC peering request #992, KMS key policy approval, Terraform networking module update",
            related_systems="payments-service, Aurora PostgreSQL, AWS KMS, VPC peering, CloudWatch",
            troubleshooting_notes=(
                "If the payments-service cannot connect, first verify the security group ingress rules and "
                "VPC route tables. Then check whether the subnet group was created in the correct AZs. "
                "If Terraform apply fails, rerun after confirming no stale state lock exists."
            ),
            reconstruction_time=None,
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
            lifecycle_stage="baton",
        )

        # Batons for Payments Legacy Migration
        legacy_migration_baton = Baton(
            project_id=payments_legacy_migration.id,
            owner_id=payment_engineer_3.id,
            successor_ids=[payment_engineer_2.id, payment_team_lead.id],
            title="Legacy Payment Gateway Decommissioning",
            description="Migrating the final 5% of traffic from the SOAP-based legacy gateway to the new REST API.",
            baton_status="completed",
            detailed_context=(
                "All 'Standard' and 'Express' merchant types have been migrated. "
                "The remaining 5% consists of 'Enterprise' clients with custom header requirements. "
                "The adapter layer is written; we just need to flip the feature flag for the 'Acme Corp' test account."
            ),
            implementation_state="Ready for Migration",
            dependencies="Enterprise client sign-off, feature flag rollout, UAT validation for Acme Corp",
            related_systems="legacy SOAP gateway, REST payments API, enterprise adapter layer, feature flag service",
            troubleshooting_notes=(
                "If enterprise traffic fails after cutover, disable the feature flag immediately and inspect "
                "header transformation logs in the adapter layer. Compare incoming SOAP headers against the "
                "expected REST contract before retrying the rollout."
            ),
            reconstruction_time=None,
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
            lifecycle_stage="baton",
        )

        # Batons for Algorithmic Trading Engine
        algo_trading_baton = Baton(
            project_id=algorithmic_trading_project.id,
            owner_id=trading_engineer_1.id,
            successor_ids=[trading_engineer_3.id, trading_team_lead.id],
            title="High-Frequency Trading Algorithm Optimization",
            description="Implementing machine learning models to optimize trade execution timing and reduce slippage.",
            baton_status="in_progress",
            detailed_context=(
                "The algorithm uses reinforcement learning to predict optimal execution windows based on market volatility. "
                "Currently integrating with Bloomberg Terminal API for real-time market data. "
                "Performance testing shows 15% improvement in execution quality but needs optimization for latency."
            ),
            implementation_state="Development",
            dependencies="Bloomberg API access approval, ML model validation, low-latency infrastructure setup",
            related_systems="Bloomberg Terminal, trading execution engine, market data feeds, ML inference pipeline",
            troubleshooting_notes=(
                "If execution latency exceeds 50ms, check network routing and consider edge computing deployment. "
                "For model accuracy issues, validate training data quality and retrain with recent market conditions. "
                "Monitor for overfitting using cross-validation metrics."
            ),
            reconstruction_time=None,
            repo_link="https://github.com/example/trading-engine",
            branch_name="feature/ml-optimization",
            daily_logs=[
                {
                    "date": "2026-04-05",
                    "note": "Completed initial ML model training with historical data.",
                },
                {
                    "date": "2026-04-06",
                    "note": "Integrated Bloomberg API and tested real-time data feed.",
                }
            ],
            additional_resources=[
                {
                    "type": "research_paper",
                    "title": "Reinforcement Learning in High-Frequency Trading",
                    "url": "https://arxiv.org/abs/2001.12345"
                },
                {
                    "type": "architecture_diagram",
                    "title": "Trading System Architecture",
                    "url": "https://lucid.app/lucidchart/trading-arch-uuid"
                },
                {
                    "type": "runbook",
                    "title": "Model Deployment Guide",
                    "url": "https://github.com/example/docs/runbooks/ml-deployment.md"
                }
            ],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            lifecycle_stage="baton",
        )

        # Batons for Real-time Risk Management
        risk_management_baton = Baton(
            project_id=risk_management_project.id,
            owner_id=trading_engineer_2.id,
            successor_ids=[trading_engineer_4.id, trading_team_lead.id],
            title="Real-time Portfolio Risk Aggregation",
            description="Building distributed system to aggregate and monitor risk metrics across all trading portfolios in real-time.",
            baton_status="awaiting_handover",
            detailed_context=(
                "System needs to handle 10,000+ concurrent risk calculations with sub-second latency. "
                "Using Apache Kafka for event streaming and Redis for caching. "
                "VaR calculations are working but need optimization for memory usage during peak hours."
            ),
            implementation_state="Testing",
            dependencies="Kafka cluster setup, Redis cluster configuration, risk model validation",
            related_systems="portfolio management system, risk calculation engine, Apache Kafka, Redis cluster",
            troubleshooting_notes=(
                "If risk calculations are delayed, check Kafka consumer lag and increase partition count if needed. "
                "For memory issues, implement data partitioning and consider horizontal scaling. "
                "Validate risk metrics against regulatory requirements before production deployment."
            ),
            reconstruction_time=None,
            repo_link="https://github.com/example/risk-engine",
            branch_name="feature/real-time-aggregation",
            daily_logs=[
                {
                    "date": "2026-04-05",
                    "note": "Completed basic risk calculation pipeline.",
                    "author": "Software Engineer"
                },
                {
                    "date": "2026-04-06",
                    "note": "Integrated Kafka streaming and tested with sample data.",
                    "author": "Software Engineer"
                }
            ],
            additional_resources=[
                {
                    "type": "regulatory_doc",
                    "title": "Risk Management Compliance Requirements",
                    "url": "https://www.sec.gov/risk-management-guidance"
                },
                {
                    "type": "runbook",
                    "title": "Risk System Failover Procedure",
                    "url": "https://github.com/example/docs/blob/main/risk-failover.md"
                },
                {
                    "type": "slack_thread",
                    "title": "Risk Team Architecture Discussion",
                    "url": "https://company.slack.com/archives/C789012/p163"
                }
            ],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            lifecycle_stage="baton",
        )

        # Batons for Cloud Infrastructure Automation
        cloud_infra_baton = Baton(
            project_id=cloud_infrastructure_project.id,
            owner_id=infra_engineer_1.id,
            successor_ids=[infra_engineer_2.id, infra_team_lead.id],
            title="Multi-Cloud Infrastructure as Code",
            description="Developing Terraform modules for automated provisioning of infrastructure across AWS, Azure, and GCP.",
            baton_status="in_progress",
            detailed_context=(
                "Modules support hybrid cloud deployments with consistent networking and security policies. "
                "Currently implementing cost optimization features and automated compliance checks. "
                "CI/CD pipeline integration is complete but needs testing with production-like environments."
            ),
            implementation_state="Development",
            dependencies="Cloud provider API access, Terraform enterprise license, security policy framework",
            related_systems="Terraform Cloud, AWS Control Tower, Azure Policy, GCP Organization, Jenkins CI/CD",
            troubleshooting_notes=(
                "For deployment failures, check cloud provider quotas and API rate limits. "
                "If compliance checks fail, review policy definitions and ensure proper tagging. "
                "Monitor Terraform state locks to prevent concurrent modification issues."
            ),
            reconstruction_time=None,
            repo_link="https://github.com/example/infrastructure-modules",
            branch_name="feature/multi-cloud-support",
            daily_logs=[
                {
                    "date": "2026-04-05",
                    "note": "Completed AWS and Azure module templates.",
                },
                {
                    "date": "2026-04-06",
                    "note": "Integrated compliance checking framework.",
                }
            ],
            additional_resources=[
                {
                    "type": "documentation",
                    "title": "Infrastructure as Code Best Practices",
                    "url": "https://cloud.google.com/docs/terraform/best-practices"
                },
                {
                    "type": "architecture_diagram",
                    "title": "Multi-Cloud Architecture",
                    "url": "https://lucid.app/lucidchart/multi-cloud-arch-uuid"
                },
                {
                    "type": "runbook",
                    "title": "Infrastructure Deployment Guide",
                    "url": "https://github.com/example/docs/runbooks/infra-deployment.md"
                }
            ],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            lifecycle_stage="baton",
        )

        # Batons for Enterprise Monitoring Systems
        monitoring_baton = Baton(
            project_id=monitoring_systems_project.id,
            owner_id=infra_engineer_3.id,
            successor_ids=[infra_engineer_4.id, infra_team_lead.id],
            title="Unified Observability Platform",
            description="Consolidating application and infrastructure monitoring into a single dashboard with AI-powered anomaly detection.",
            baton_status="in_progress",
            detailed_context=(
                "Platform integrates Prometheus, Grafana, and ELK stack with custom ML models for predictive alerting. "
                "Currently setting up data pipelines for log aggregation and metric correlation. "
                "User interface design is complete but backend API needs performance optimization."
            ),
            implementation_state="Integration Testing",
            dependencies="Prometheus federation setup, ELK cluster configuration, ML model training data",
            related_systems="Prometheus, Grafana, Elasticsearch, Logstash, Kibana, ML inference service",
            troubleshooting_notes=(
                "If dashboards load slowly, check Elasticsearch query performance and consider index optimization. "
                "For false positive alerts, review ML model thresholds and retrain with more diverse data. "
                "Ensure proper data retention policies to manage storage costs."
            ),
            reconstruction_time=None,
            repo_link="https://github.com/example/observability-platform",
            branch_name="feature/ai-anomaly-detection",
            daily_logs=[
                {
                    "date": "2026-04-05",
                    "note": "Completed Prometheus metric collection setup.",
                    "author": "Software Engineer"
                },
                {
                    "date": "2026-04-06",
                    "note": "Integrated basic ML anomaly detection.",
                    "author": "Software Engineer"
                }
            ],
            additional_resources=[
                {
                    "type": "guide",
                    "title": "Observability Best Practices",
                    "url": "https://opentelemetry.io/docs/concepts/observability-principles/"
                },
                {
                    "type": "runbook",
                    "title": "Monitoring System Recovery",
                    "url": "https://github.com/example/docs/blob/main/monitoring-recovery.md"
                },
                {
                    "type": "slack_thread",
                    "title": "Observability Platform Design Review",
                    "url": "https://company.slack.com/archives/C345678/p164"
                }
            ],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            lifecycle_stage="baton",
        )

        # Additional Batons for Payment Platform Team
        payment_api_baton = Baton(
            project_id=payment_aws_project.id,
            owner_id=payment_engineer_2.id,
            successor_ids=[payment_engineer_4.id, payment_team_lead.id],
            title="Payment API Rate Limiting Implementation",
            description="Implementing distributed rate limiting for payment APIs to prevent abuse and ensure fair usage.",
            baton_status="in_progress",
            detailed_context=(
                "Using Redis-based rate limiting with sliding window algorithm. "
                "Need to handle distributed requests across multiple API gateways. "
                "Currently testing with synthetic load but need to validate with real traffic patterns."
            ),
            implementation_state="Development",
            dependencies="Redis cluster setup, API gateway configuration, load testing environment",
            related_systems="API Gateway, Redis Cluster, Payment Service, Monitoring Dashboard",
            troubleshooting_notes=(
                "If rate limits are too restrictive, check Redis connection pooling and key expiration. "
                "For distributed consistency issues, verify NTP synchronization across servers. "
                "Monitor Redis memory usage to prevent eviction of rate limit keys."
            ),
            reconstruction_time=None,
            repo_link="https://github.com/example/payment-api",
            branch_name="feature/rate-limiting",
            daily_logs=[
                {
                    "date": "2026-04-07",
                    "note": "Implemented basic Redis rate limiter.",
                },
                {
                    "date": "2026-04-08",
                    "note": "Added distributed sliding window logic.",
                }
            ],
            additional_resources=[
                {
                    "type": "documentation",
                    "title": "Rate Limiting Best Practices",
                    "url": "https://cloud.google.com/api-gateway/docs/rate-limiting"
                },
                {
                    "type": "runbook",
                    "title": "Redis Cluster Maintenance",
                    "url": "https://github.com/example/docs/runbooks/redis-maintenance.md"
                }
            ],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            lifecycle_stage="baton",
        )

        payment_security_baton = Baton(
            project_id=payments_legacy_migration.id,
            owner_id=payment_engineer_4.id,
            successor_ids=[payment_engineer_1.id, payment_resilience_manager.id],
            title="Payment Data Encryption Standards Update",
            description="Upgrading encryption standards for payment data to comply with latest PCI DSS requirements.",
            baton_status="in_progress",
            detailed_context=(
                "Moving from AES-256 to AES-256-GCM for authenticated encryption. "
                "Need to update key rotation policies and implement perfect forward secrecy. "
                "Legacy systems still using older encryption methods need migration path."
            ),
            implementation_state="Security Review",
            dependencies="Security team approval, key management system update, compliance audit",
            related_systems="Payment Database, Key Management Service, Security Monitoring, PCI DSS Framework",
            troubleshooting_notes=(
                "If decryption fails after key rotation, check key versioning and ensure proper key retrieval. "
                "For performance issues with GCM, consider hardware acceleration options. "
                "Validate encryption with test vectors before production deployment."
            ),
            reconstruction_time=None,
            repo_link="https://github.com/example/payment-security",
            branch_name="feature/aes-gcm-upgrade",
            daily_logs=[
                {
                    "date": "2026-04-07",
                    "note": "Completed AES-GCM implementation.",
                    "author": "Software Engineer"
                },
                {
                    "date": "2026-04-08",
                    "note": "Passed initial security review.",
                    "author": "Software Engineer"
                }
            ],
            additional_resources=[
                {
                    "type": "compliance_doc",
                    "title": "PCI DSS Encryption Requirements",
                    "url": "https://www.pcisecuritystandards.org/document_library"
                },
                {
                    "type": "runbook",
                    "title": "Key Rotation Procedure",
                    "url": "https://github.com/example/docs/runbooks/key-rotation.md"
                }
            ],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            lifecycle_stage="baton",
        )

        payment_team_lead_baton = Baton(
            project_id=payment_aws_project.id,
            owner_id=payment_team_lead.id,
            successor_ids=[payment_resilience_manager.id],
            title="Payment Platform Architecture Review",
            description="Leading architecture review for payment platform scalability improvements.",
            baton_status="completed",
            detailed_context=(
                "Reviewing current architecture for handling 10x traffic growth. "
                "Evaluating microservices decomposition and event-driven architecture options. "
                "Need to present recommendations to CTO and get stakeholder alignment."
            ),
            implementation_state="Planning",
            dependencies="Stakeholder interviews, performance benchmarking, cost analysis",
            related_systems="Payment Platform, Load Balancer, Database Cluster, CDN",
            troubleshooting_notes=(
                "If architecture recommendations are rejected, prepare alternative solutions with pros/cons. "
                "For cost concerns, provide detailed ROI calculations and migration timelines. "
                "Ensure all recommendations include rollback plans."
            ),
            reconstruction_time=None,
            repo_link="https://github.com/example/payment-arch",
            branch_name="feature/architecture-review",
            daily_logs=[
                {
                    "date": "2026-04-07",
                    "note": "Completed stakeholder interviews.",
                },
                {
                    "date": "2026-04-08",
                    "note": "Drafted initial architecture recommendations.",
                }
            ],
            additional_resources=[
                {
                    "type": "presentation",
                    "title": "Payment Platform Scalability Analysis",
                    "url": "https://docs.google.com/presentation/architecture-review-456"
                },
                {
                    "type": "spreadsheet",
                    "title": "Cost-Benefit Analysis",
                    "url": "https://docs.google.com/spreadsheets/cost-analysis-789"
                }
            ],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            lifecycle_stage="baton",
        )

        payment_team_lead_baton_2 = Baton(
            project_id=payments_legacy_migration.id,
            owner_id=payment_team_lead.id,
            successor_ids=[payment_engineer_1.id],
            title="Team Performance Optimization Initiative",
            description="Leading team-wide initiative to improve development processes and productivity.",
            baton_status="in_progress",
            detailed_context=(
                "Analyzing current development workflows and identifying bottlenecks. "
                "Implementing agile practices and continuous improvement processes. "
                "Working on establishing metrics for team performance tracking."
            ),
            implementation_state="Implementation",
            dependencies="Team feedback sessions, process documentation, tool evaluation",
            related_systems="Development Tools, CI/CD Pipeline, Project Management, Code Quality Tools",
            troubleshooting_notes=(
                "If process changes face resistance, focus on quick wins and gradual implementation. "
                "For tool adoption issues, provide comprehensive training and support. "
                "Measure impact regularly and adjust approach based on feedback."
            ),
            reconstruction_time=None,
            repo_link="https://github.com/example/team-process",
            branch_name="feature/process-optimization",
            daily_logs=[
                {
                    "date": "2026-04-09",
                    "note": "Completed team feedback survey.",
                },
                {
                    "date": "2026-04-10",
                    "note": "Identified key improvement areas.",
                }
            ],
            additional_resources=[
                {
                    "type": "survey_results",
                    "title": "Team Process Feedback",
                    "url": "https://docs.google.com/survey-results-404"
                },
                {
                    "type": "guide",
                    "title": "Agile Development Best Practices",
                    "url": "https://www.agilealliance.org/agile101/"
                }
            ],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            lifecycle_stage="baton",
        )

        # Additional Batons for Trading Systems Team
        trading_risk_baton = Baton(
            project_id=risk_management_project.id,
            owner_id=trading_engineer_2.id,
            successor_ids=[trading_engineer_4.id, trading_team_lead.id],
            title="Real-time Market Risk Dashboard",
            description="Building real-time dashboard for monitoring market risk exposure across all trading books.",
            baton_status="in_progress",
            detailed_context=(
                "Dashboard needs to aggregate risk metrics from multiple trading systems with sub-second latency. "
                "Implementing WebSocket connections for real-time updates. "
                "Currently facing challenges with data consistency across distributed systems."
            ),
            implementation_state="Development",
            dependencies="Trading system APIs, WebSocket infrastructure, real-time data pipeline",
            related_systems="Trading Systems, Risk Engine, WebSocket Server, Real-time Database",
            troubleshooting_notes=(
                "If dashboard shows stale data, check WebSocket connection health and message queuing. "
                "For performance issues, implement data sampling and aggregation caching. "
                "Validate risk calculations against manual calculations for accuracy."
            ),
            reconstruction_time=None,
            repo_link="https://github.com/example/trading-dashboard",
            branch_name="feature/risk-dashboard",
            daily_logs=[
                {
                    "date": "2026-04-07",
                    "note": "Implemented basic WebSocket connections.",
                },
                {
                    "date": "2026-04-08",
                    "note": "Added risk metric aggregation logic.",
                }
            ],
            additional_resources=[
                {
                    "type": "ui_mockups",
                    "title": "Dashboard Wireframes",
                    "url": "https://figma.com/dashboard-mockups-123"
                },
                {
                    "type": "api_docs",
                    "title": "Trading System APIs",
                    "url": "https://developer.example.com/trading-apis"
                }
            ],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            lifecycle_stage="baton",
        )

        trading_ml_baton = Baton(
            project_id=algorithmic_trading_project.id,
            owner_id=trading_engineer_3.id,
            successor_ids=[trading_engineer_1.id, trading_team_lead.id],
            title="Machine Learning Model Validation Framework",
            description="Developing comprehensive validation framework for trading ML models including backtesting and live testing.",
            baton_status="in_progress",
            detailed_context=(
                "Framework needs to handle multiple model types and validation scenarios. "
                "Implementing statistical significance testing and performance attribution. "
                "Currently working on integration with existing backtesting infrastructure."
            ),
            implementation_state="Testing",
            dependencies="Backtesting platform integration, statistical libraries, model registry",
            related_systems="ML Platform, Backtesting Engine, Model Registry, Statistical Analysis Tools",
            troubleshooting_notes=(
                "If validation results are inconsistent, check data preprocessing and feature engineering. "
                "For performance attribution issues, verify trade execution data quality. "
                "Ensure all models pass minimum performance thresholds before live deployment."
            ),
            reconstruction_time=None,
            repo_link="https://github.com/example/ml-validation",
            branch_name="feature/model-validation",
            daily_logs=[
                {
                    "date": "2026-04-07",
                    "note": "Completed statistical testing framework.",
                    "author": "Software Engineer"
                },
                {
                    "date": "2026-04-08",
                    "note": "Integrated with backtesting platform.",
                    "author": "Software Engineer"
                }
            ],
            additional_resources=[
                {
                    "type": "research_paper",
                    "title": "ML Model Validation in Finance",
                    "url": "https://arxiv.org/abs/2101.56789"
                },
                {
                    "type": "runbook",
                    "title": "Model Deployment Checklist",
                    "url": "https://github.com/example/docs/runbooks/ml-deployment-checklist.md"
                }
            ],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            lifecycle_stage="baton",
        )

        trading_team_lead_baton = Baton(
            project_id=algorithmic_trading_project.id,
            owner_id=trading_team_lead.id,
            successor_ids=[trading_engineer_1.id],
            title="Trading System Performance Optimization",
            description="Leading initiative to optimize trading system performance for high-frequency operations.",
            baton_status="in_progress",
            detailed_context=(
                "Analyzing current bottlenecks in order processing pipeline. "
                "Evaluating kernel bypass technologies and hardware acceleration options. "
                "Need to coordinate with infrastructure team for hardware upgrades."
            ),
            implementation_state="Analysis",
            dependencies="Performance profiling tools, infrastructure team coordination, hardware evaluation",
            related_systems="Trading Engine, Network Infrastructure, Hardware Acceleration, Order Routing",
            troubleshooting_notes=(
                "If performance improvements are marginal, consider algorithmic optimizations first. "
                "For hardware bottlenecks, document current vs required specifications. "
                "Ensure all optimizations maintain system reliability and compliance."
            ),
            reconstruction_time=None,
            repo_link="https://github.com/example/trading-performance",
            branch_name="feature/performance-optimization",
            daily_logs=[
                {
                    "date": "2026-04-07",
                    "note": "Completed initial performance profiling.",
                },
                {
                    "date": "2026-04-08",
                    "note": "Identified key bottlenecks in order processing.",
                }
            ],
            additional_resources=[
                {
                    "type": "benchmark_report",
                    "title": "Trading System Performance Analysis",
                    "url": "https://docs.google.com/benchmark-report-101"
                },
                {
                    "type": "architecture_diagram",
                    "title": "High-Frequency Trading Architecture",
                    "url": "https://lucid.app/lucidchart/hft-arch-uuid"
                }
            ],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            lifecycle_stage="baton",
        )

        # Additional Batons for Infrastructure Team
        infra_security_baton = Baton(
            project_id=cloud_infrastructure_project.id,
            owner_id=infra_engineer_1.id,
            successor_ids=[infra_engineer_2.id, infra_team_lead.id],
            title="Cloud Security Posture Management",
            description="Implementing automated security posture management across multi-cloud infrastructure.",
            baton_status="in_progress",
            detailed_context=(
                "Setting up continuous compliance monitoring and automated remediation. "
                "Integrating with cloud security tools and implementing policy as code. "
                "Currently working on AWS Config and Azure Policy integration."
            ),
            implementation_state="Development",
            dependencies="Cloud security tools integration, policy framework, automated remediation",
            related_systems="AWS Config, Azure Policy, GCP Security Command Center, Policy Engine",
            troubleshooting_notes=(
                "If compliance checks fail unexpectedly, verify policy definitions and resource tagging. "
                "For remediation conflicts, implement approval workflows for critical changes. "
                "Monitor for false positives and tune policy rules accordingly."
            ),
            reconstruction_time=None,
            repo_link="https://github.com/example/cloud-security",
            branch_name="feature/security-posture",
            daily_logs=[
                {
                    "date": "2026-04-07",
                    "note": "Set up AWS Config rules.",
                },
                {
                    "date": "2026-04-08",
                    "note": "Implemented basic remediation workflows.",
                }
            ],
            additional_resources=[
                {
                    "type": "security_guide",
                    "title": "Cloud Security Best Practices",
                    "url": "https://cloud.google.com/security/best-practices"
                },
                {
                    "type": "runbook",
                    "title": "Security Incident Response",
                    "url": "https://github.com/example/docs/runbooks/security-incident.md"
                }
            ],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            lifecycle_stage="baton",
        )

        infra_monitoring_baton = Baton(
            project_id=monitoring_systems_project.id,
            owner_id=infra_engineer_3.id,
            successor_ids=[infra_engineer_4.id, infra_team_lead.id],
            title="Distributed Tracing Implementation",
            description="Implementing distributed tracing across microservices for better observability and debugging.",
            baton_status="awaiting_handover",
            detailed_context=(
                "Using OpenTelemetry for standardized tracing across all services. "
                "Setting up Jaeger for trace collection and visualization. "
                "Need to instrument existing services and establish tracing best practices."
            ),
            implementation_state="Integration Testing",
            dependencies="OpenTelemetry SDK integration, Jaeger deployment, service instrumentation",
            related_systems="Microservices, OpenTelemetry, Jaeger, Log Aggregation, Metrics Collection",
            troubleshooting_notes=(
                "If traces are incomplete, check OpenTelemetry auto-instrumentation coverage. "
                "For performance impact, implement sampling strategies and resource limits. "
                "Validate trace correlation across service boundaries."
            ),
            reconstruction_time=None,
            repo_link="https://github.com/example/distributed-tracing",
            branch_name="feature/opentelemetry-tracing",
            daily_logs=[
                {
                    "date": "2026-04-07",
                    "note": "Completed OpenTelemetry setup.",
                    "author": "Software Engineer"
                },
                {
                    "date": "2026-04-08",
                    "note": "Instrumented first set of services.",
                    "author": "Software Engineer"
                }
            ],
            additional_resources=[
                {
                    "type": "documentation",
                    "title": "OpenTelemetry Best Practices",
                    "url": "https://opentelemetry.io/docs/concepts/best-practices/"
                },
                {
                    "type": "runbook",
                    "title": "Tracing Troubleshooting Guide",
                    "url": "https://github.com/example/docs/runbooks/tracing-troubleshooting.md"
                }
            ],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            lifecycle_stage="baton",
        )

        infra_team_lead_baton = Baton(
            project_id=cloud_infrastructure_project.id,
            owner_id=infra_team_lead.id,
            successor_ids=[infra_engineer_1.id],
            title="Infrastructure Cost Optimization Initiative",
            description="Leading company-wide initiative to optimize cloud infrastructure costs while maintaining performance.",
            baton_status="in_progress",
            detailed_context=(
                "Analyzing current cloud spending patterns and identifying optimization opportunities. "
                "Implementing automated resource scaling and reserved instance strategies. "
                "Need to balance cost savings with system reliability requirements."
            ),
            implementation_state="Planning",
            dependencies="Cost analysis tools, stakeholder alignment, automation frameworks",
            related_systems="Cloud Cost Management, Auto Scaling, Reserved Instances, Resource Monitoring",
            troubleshooting_notes=(
                "If cost optimizations impact performance, implement gradual rollout with monitoring. "
                "For reserved instance recommendations, validate usage patterns over time. "
                "Ensure all optimizations have clear rollback procedures."
            ),
            reconstruction_time=None,
            repo_link="https://github.com/example/cost-optimization",
            branch_name="feature/cost-optimization",
            daily_logs=[
                {
                    "date": "2026-04-07",
                    "note": "Completed initial cost analysis.",
                },
                {
                    "date": "2026-04-08",
                    "note": "Identified key optimization opportunities.",
                }
            ],
            additional_resources=[
                {
                    "type": "spreadsheet",
                    "title": "Cloud Cost Analysis",
                    "url": "https://docs.google.com/spreadsheets/cost-analysis-202"
                },
                {
                    "type": "presentation",
                    "title": "Cost Optimization Strategy",
                    "url": "https://docs.google.com/presentation/cost-strategy-303"
                }
            ],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            lifecycle_stage="baton",
        )

        # More batons for various team members
        payment_fraud_baton = Baton(
            project_id=payments_legacy_migration.id,
            owner_id=payment_engineer_1.id,
            successor_ids=[payment_engineer_3.id, payment_team_lead.id],
            title="Advanced Fraud Detection System",
            description="Implementing machine learning-based fraud detection for payment transactions.",
            baton_status="in_progress",
            detailed_context=(
                "Using anomaly detection algorithms to identify fraudulent patterns. "
                "Training on historical transaction data with labeled fraud cases. "
                "Need to balance false positives with fraud detection accuracy."
            ),
            implementation_state="Development",
            dependencies="ML model training, transaction data access, real-time scoring infrastructure",
            related_systems="Payment Processing, ML Platform, Fraud Database, Alert System",
            troubleshooting_notes=(
                "If false positive rate is high, adjust model thresholds and retrain with more data. "
                "For real-time scoring delays, optimize model inference and implement caching. "
                "Regularly validate model performance against known fraud cases."
            ),
            reconstruction_time=None,
            repo_link="https://github.com/example/fraud-detection",
            branch_name="feature/ml-fraud-detection",
            daily_logs=[
                {
                    "date": "2026-04-09",
                    "note": "Completed initial model training.",
                },
                {
                    "date": "2026-04-10",
                    "note": "Implemented real-time scoring pipeline.",
                }
            ],
            additional_resources=[
                {
                    "type": "research_paper",
                    "title": "Machine Learning for Fraud Detection",
                    "url": "https://arxiv.org/abs/2201.98765"
                },
                {
                    "type": "dataset",
                    "title": "Fraud Detection Training Data",
                    "url": "https://data.example.com/fraud-dataset"
                }
            ],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            lifecycle_stage="baton",
        )

        trading_backtest_baton = Baton(
            project_id=algorithmic_trading_project.id,
            owner_id=trading_engineer_4.id,
            successor_ids=[trading_engineer_2.id, trading_team_lead.id],
            title="Advanced Backtesting Framework",
            description="Building sophisticated backtesting framework with realistic market conditions simulation.",
            baton_status="awaiting_handover",
            detailed_context=(
                "Framework includes slippage modeling, market impact simulation, and transaction costs. "
                "Implementing parallel processing for faster backtesting execution. "
                "Need to validate results against live trading performance."
            ),
            implementation_state="Testing",
            dependencies="Historical market data, parallel processing framework, validation tools",
            related_systems="Backtesting Engine, Market Data, Trading Strategies, Performance Analytics",
            troubleshooting_notes=(
                "If backtesting results don't match live performance, check slippage and cost assumptions. "
                "For slow execution, optimize parallel processing and data access patterns. "
                "Ensure all backtests include realistic trading constraints."
            ),
            reconstruction_time=None,
            repo_link="https://github.com/example/backtesting-framework",
            branch_name="feature/advanced-backtesting",
            daily_logs=[
                {
                    "date": "2026-04-09",
                    "note": "Implemented slippage modeling.",
                    "author": "Software Engineer"
                },
                {
                    "date": "2026-04-10",
                    "note": "Added parallel processing support.",
                    "author": "Software Engineer"
                }
            ],
            additional_resources=[
                {
                    "type": "documentation",
                    "title": "Backtesting Best Practices",
                    "url": "https://www.quantopian.com/docs/backtesting"
                },
                {
                    "type": "runbook",
                    "title": "Backtesting Validation Procedure",
                    "url": "https://github.com/example/docs/runbooks/backtesting-validation.md"
                }
            ],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            lifecycle_stage="baton",
        )

        infra_container_baton = Baton(
            project_id=cloud_infrastructure_project.id,
            owner_id=infra_engineer_2.id,
            successor_ids=[infra_engineer_3.id, infra_team_lead.id],
            title="Kubernetes Cluster Optimization",
            description="Optimizing Kubernetes clusters for cost efficiency and performance across production workloads.",
            baton_status="in_progress",
            detailed_context=(
                "Analyzing resource utilization and implementing right-sizing recommendations. "
                "Setting up horizontal pod autoscaling and cluster autoscaling. "
                "Working on implementing spot instances for non-critical workloads."
            ),
            implementation_state="Implementation",
            dependencies="Kubernetes metrics, cost monitoring, workload profiling",
            related_systems="Kubernetes Clusters, Prometheus, Cost Management, Workload Scheduler",
            troubleshooting_notes=(
                "If autoscaling causes instability, review HPA configurations and resource requests. "
                "For spot instance interruptions, implement graceful shutdown procedures. "
                "Monitor for cost savings vs performance trade-offs."
            ),
            reconstruction_time=None,
            repo_link="https://github.com/example/k8s-optimization",
            branch_name="feature/cluster-optimization",
            daily_logs=[
                {
                    "date": "2026-04-09",
                    "note": "Completed resource utilization analysis.",
                },
                {
                    "date": "2026-04-10",
                    "note": "Implemented HPA for critical services.",
                }
            ],
            additional_resources=[
                {
                    "type": "guide",
                    "title": "Kubernetes Cost Optimization",
                    "url": "https://cloud.google.com/kubernetes-engine/docs/cost-optimization"
                },
                {
                    "type": "runbook",
                    "title": "Cluster Scaling Procedures",
                    "url": "https://github.com/example/docs/runbooks/cluster-scaling.md"
                }
            ],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            lifecycle_stage="baton",
        )

        payment_mobile_baton = Baton(
            project_id=payment_aws_project.id,
            owner_id=payment_engineer_3.id,
            successor_ids=[payment_engineer_4.id, payment_team_lead.id],
            title="Mobile Payment SDK Development",
            description="Developing cross-platform SDK for mobile payment integration.",
            baton_status="awaiting_handover",
            detailed_context=(
                "SDK needs to support iOS and Android with consistent API. "
                "Implementing secure tokenization and biometric authentication. "
                "Currently working on native bridge implementations."
            ),
            implementation_state="Development",
            dependencies="Mobile development frameworks, security libraries, testing devices",
            related_systems="Mobile Apps, Payment Gateway, Security Services, Biometric Systems",
            troubleshooting_notes=(
                "If SDK integration fails, check native bridge implementations and API compatibility. "
                "For security issues, validate tokenization and encryption implementations. "
                "Test on various device configurations and OS versions."
            ),
            reconstruction_time=None,
            repo_link="https://github.com/example/mobile-payment-sdk",
            branch_name="feature/cross-platform-sdk",
            daily_logs=[
                {
                    "date": "2026-04-09",
                    "note": "Completed iOS implementation.",
                    "author": "Software Engineer"
                },
                {
                    "date": "2026-04-10",
                    "note": "Started Android implementation.",
                    "author": "Software Engineer"
                }
            ],
            additional_resources=[
                {
                    "type": "api_docs",
                    "title": "Mobile Payment SDK API",
                    "url": "https://developer.example.com/mobile-sdk"
                },
                {
                    "type": "runbook",
                    "title": "SDK Integration Guide",
                    "url": "https://github.com/example/docs/runbooks/sdk-integration.md"
                }
            ],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            lifecycle_stage="baton",
        )

        trading_compliance_baton = Baton(
            project_id=risk_management_project.id,
            owner_id=trading_engineer_1.id,
            successor_ids=[trading_engineer_3.id, trading_team_lead.id],
            title="Regulatory Reporting Automation",
            description="Automating regulatory reporting processes for trading activities.",
            baton_status="in_progress",
            detailed_context=(
                "Implementing automated generation of trade reports for regulatory compliance. "
                "Integrating with multiple regulatory systems and data sources. "
                "Need to ensure data accuracy and timely submission."
            ),
            implementation_state="Development",
            dependencies="Regulatory APIs, data validation, automated scheduling",
            related_systems="Trading Systems, Regulatory Databases, Report Generation, Audit Systems",
            troubleshooting_notes=(
                "If reports contain errors, validate data sources and transformation logic. "
                "For submission delays, check API rate limits and implement retry mechanisms. "
                "Maintain audit trails for all automated report generation."
            ),
            reconstruction_time=None,
            repo_link="https://github.com/example/regulatory-reporting",
            branch_name="feature/automated-reporting",
            daily_logs=[
                {
                    "date": "2026-04-09",
                    "note": "Completed initial report templates.",
                },
                {
                    "date": "2026-04-10",
                    "note": "Integrated with regulatory APIs.",
                }
            ],
            additional_resources=[
                {
                    "type": "regulatory_guide",
                    "title": "Trading Reporting Requirements",
                    "url": "https://www.sec.gov/trading-reports"
                },
                {
                    "type": "runbook",
                    "title": "Report Generation Procedure",
                    "url": "https://github.com/example/docs/runbooks/report-generation.md"
                }
            ],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            lifecycle_stage="baton",
        )

        infra_backup_baton = Baton(
            project_id=monitoring_systems_project.id,
            owner_id=infra_engineer_4.id,
            successor_ids=[infra_engineer_1.id, infra_team_lead.id],
            title="Disaster Recovery Automation",
            description="Implementing automated disaster recovery procedures for critical systems.",
            baton_status="in_progress",
            detailed_context=(
                "Setting up automated failover and data recovery processes. "
                "Testing recovery time objectives and recovery point objectives. "
                "Need to coordinate with business continuity team."
            ),
            implementation_state="Testing",
            dependencies="Backup systems, failover infrastructure, testing environments",
            related_systems="Backup Storage, Failover Systems, Monitoring, Alert Management",
            troubleshooting_notes=(
                "If recovery fails, check backup integrity and restore procedures. "
                "For RTO/RPO violations, optimize recovery processes and resource allocation. "
                "Document all recovery steps and validate with regular testing."
            ),
            reconstruction_time=None,
            repo_link="https://github.com/example/disaster-recovery",
            branch_name="feature/automated-dr",
            daily_logs=[
                {
                    "date": "2026-04-09",
                    "note": "Completed failover automation.",
                    "author": "Software Engineer"
                },
                {
                    "date": "2026-04-10",
                    "note": "Tested recovery procedures.",
                    "author": "Software Engineer"
                }
            ],
            additional_resources=[
                {
                    "type": "runbook",
                    "title": "Disaster Recovery Procedures",
                    "url": "https://github.com/example/docs/runbooks/disaster-recovery.md"
                },
                {
                    "type": "compliance_doc",
                    "title": "Business Continuity Requirements",
                    "url": "https://www.iso.org/business-continuity"
                }
            ],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            lifecycle_stage="baton",
        )

        # Extra seeded batons to provide additional examples across every workflow status.
        workflow_expansion_specs = [
            {
                "project_id": payment_aws_project.id,
                "owner_id": payment_engineer_2.id,
                "successor_ids": [payment_engineer_1.id, payment_team_lead.id],
                "title": "Payment Token Vault Reliability Improvements",
                "description": "Hardening token vault failover and reducing p95 token retrieval latency for checkout paths.",
                "detailed_context": (
                    "Primary and secondary vault nodes are deployed, but failover health checks need tighter thresholds. "
                    "Canary tests show improved resilience under node restarts."
                ),
                "implementation_state": "Testing",
                "dependencies": "Vault failover probes, checkout canary scenarios, security sign-off",
                "related_systems": "token-vault, checkout-service, health-probe-agent, secrets-manager",
                "troubleshooting_notes": (
                    "When token retrieval latency spikes, inspect vault replication lag and retry queue depth "
                    "before rolling back probe thresholds."
                ),
                "repo_link": "https://github.com/example/payment-token-vault",
                "branch_name": "feature/vault-reliability",
            },
            {
                "project_id": payments_legacy_migration.id,
                "owner_id": payment_engineer_4.id,
                "successor_ids": [payment_engineer_2.id, payment_team_lead.id],
                "title": "Merchant Settlement Reconciliation Rewrite",
                "description": "Replacing nightly settlement reconciliation with streaming reconciliation and exception queues.",
                "detailed_context": (
                    "Streaming reconciliation consumer is stable in staging, but settlement mismatch triage UI "
                    "still needs role-based access checks."
                ),
                "implementation_state": "Development",
                "dependencies": "settlement event stream contracts, reconciliation UI auth rules, finance UAT",
                "related_systems": "settlement-stream, reconciliation-worker, finance-dashboard, audit-store",
                "troubleshooting_notes": (
                    "If mismatch volume spikes after deploy, validate event schema versions and replay the "
                    "failed partitions from the last stable offset."
                ),
                "repo_link": "https://github.com/example/settlement-reconciliation",
                "branch_name": "feature/streaming-reconciliation",
            },
            {
                "project_id": algorithmic_trading_project.id,
                "owner_id": trading_engineer_3.id,
                "successor_ids": [trading_engineer_1.id, trading_team_lead.id],
                "title": "Strategy Risk Guardrails Service",
                "description": "Adding pre-trade guardrails service to block invalid orders before exchange submission.",
                "detailed_context": (
                    "Guardrail checks for max notional and volatility envelopes are implemented. "
                    "Exchange adapter hooks need soak testing under opening-auction burst traffic."
                ),
                "implementation_state": "Integration Testing",
                "dependencies": "exchange adapter hooks, guardrail policy config, soak-test infra",
                "related_systems": "order-router, strategy-engine, guardrail-service, policy-store",
                "troubleshooting_notes": (
                    "If legitimate orders are blocked, inspect policy cache staleness and compare with "
                    "latest signed policy bundle."
                ),
                "repo_link": "https://github.com/example/strategy-guardrails",
                "branch_name": "feature/pretrade-guardrails",
            },
            {
                "project_id": risk_management_project.id,
                "owner_id": trading_engineer_1.id,
                "successor_ids": [trading_engineer_3.id, trading_team_lead.id],
                "title": "Stress Test Scenario Automation",
                "description": "Automating portfolio stress scenarios for intraday risk recalculation and alerting.",
                "detailed_context": (
                    "Scenario templates for macro shocks are in place. "
                    "Need to finish drift checks comparing stress outputs against baseline VaR snapshots."
                ),
                "implementation_state": "Development",
                "dependencies": "scenario template approvals, baseline VaR snapshots, alert routing updates",
                "related_systems": "stress-engine, var-calculator, scenario-library, alert-router",
                "troubleshooting_notes": (
                    "For noisy alerts, tighten drift thresholds by portfolio class and verify input snapshot "
                    "timestamps are aligned."
                ),
                "repo_link": "https://github.com/example/stress-automation",
                "branch_name": "feature/stress-scenarios",
            },
            {
                "project_id": cloud_infrastructure_project.id,
                "owner_id": infra_engineer_2.id,
                "successor_ids": [infra_engineer_1.id, infra_team_lead.id],
                "title": "Cluster Upgrade Orchestration Pipeline",
                "description": "Automating Kubernetes minor version upgrades with phased node-pool rollout policies.",
                "detailed_context": (
                    "Upgrade orchestration supports canary node pools and rollback triggers. "
                    "Need to finalize maintenance window coordination with service owners."
                ),
                "implementation_state": "Testing",
                "dependencies": "cluster maintenance windows, rollback policy validation, workload disruption reports",
                "related_systems": "kubernetes-control-plane, rollout-orchestrator, disruption-monitor, incident-bot",
                "troubleshooting_notes": (
                    "If node-pool drain stalls, inspect PodDisruptionBudget constraints and force-evict only "
                    "after confirming replica health."
                ),
                "repo_link": "https://github.com/example/cluster-upgrades",
                "branch_name": "feature/upgrade-orchestration",
            },
            {
                "project_id": monitoring_systems_project.id,
                "owner_id": infra_engineer_4.id,
                "successor_ids": [infra_engineer_3.id, infra_team_lead.id],
                "title": "Alert Noise Reduction Program",
                "description": "Reducing duplicate and low-signal alerts by tuning routing rules and dedupe windows.",
                "detailed_context": (
                    "Top 30 noisy alerts are catalogued and partially tuned. "
                    "Escalation policy backtests still required for off-hours reliability."
                ),
                "implementation_state": "Implementation",
                "dependencies": "alert routing policy updates, historical alert replay, on-call sign-off",
                "related_systems": "alert-manager, pager-routing, observability-stack, oncall-roster",
                "troubleshooting_notes": (
                    "If critical incidents are suppressed, rollback dedupe window changes and review "
                    "severity mappings before reapplying."
                ),
                "repo_link": "https://github.com/example/alert-noise-reduction",
                "branch_name": "feature/alert-dedupe",
            },
            {
                "project_id": payment_aws_project.id,
                "owner_id": payment_team_lead.id,
                "successor_ids": [payment_engineer_1.id, payment_engineer_2.id],
                "title": "Card Routing Incident Readiness",
                "description": "Running incident readiness drills for card-routing outages and regional fallback playbooks.",
                "detailed_context": (
                    "Primary outage simulation scripts are complete with region-level failover checks. "
                    "Need final approvals from platform operations for production rehearsal."
                ),
                "implementation_state": "Planning",
                "dependencies": "incident drill approvals, fallback runbook sign-off, operations rehearsal slot",
                "related_systems": "card-router, fallback-gateway, incident-automation, status-dashboard",
                "troubleshooting_notes": (
                    "If drill outcomes diverge from expected fallback timing, compare routing rule propagation "
                    "latency across regions."
                ),
                "repo_link": "https://github.com/example/card-routing-readiness",
                "branch_name": "feature/incident-readiness",
            },
            {
                "project_id": risk_management_project.id,
                "owner_id": trading_team_lead.id,
                "successor_ids": [trading_engineer_2.id, trading_engineer_4.id],
                "title": "Desk Limit Breach Escalation Workflow",
                "description": "Standardizing desk limit breach triage workflow with automated owner assignment and escalation.",
                "detailed_context": (
                    "Escalation matrix is codified and integrated with desk metadata. "
                    "Still validating assignment fairness under simultaneous breach events."
                ),
                "implementation_state": "Testing",
                "dependencies": "desk ownership metadata, escalation rules QA, incident channel automation",
                "related_systems": "limit-monitor, desk-registry, escalation-engine, incident-channel-bot",
                "troubleshooting_notes": (
                    "If assignments skew to a single responder, verify desk grouping logic and "
                    "round-robin state persistence."
                ),
                "repo_link": "https://github.com/example/breach-escalation",
                "branch_name": "feature/escalation-workflow",
            },
        ]

        workflow_expansion_batons = [
            Baton(
                project_id=spec["project_id"],
                owner_id=spec["owner_id"],
                successor_ids=spec["successor_ids"],
                title=spec["title"],
                description=spec["description"],
                baton_status="in_progress",
                detailed_context=spec["detailed_context"],
                implementation_state=spec["implementation_state"],
                dependencies=spec["dependencies"],
                related_systems=spec["related_systems"],
                troubleshooting_notes=spec["troubleshooting_notes"],
                reconstruction_time=None,
                repo_link=spec["repo_link"],
                branch_name=spec["branch_name"],
                daily_logs=[
                    {
                        "date": "2026-04-11",
                        "note": "Kickoff complete and scope validated with stakeholders.",
                    },
                    {
                        "date": "2026-04-12",
                        "note": "First implementation milestone delivered and reviewed.",
                    },
                ],
                additional_resources=[
                    {
                        "type": "runbook",
                        "title": f"{spec['title']} Runbook",
                        "url": "https://github.com/example/docs/runbooks/workflow-expansion",
                    },
                    {
                        "type": "architecture_diagram",
                        "title": f"{spec['title']} Architecture",
                        "url": "https://lucid.app/lucidchart/workflow-expansion",
                    },
                ],
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc),
                lifecycle_stage="baton",
            )
            for spec in workflow_expansion_specs
        ]

        all_batons = [
            payment_aws_baton, legacy_migration_baton,
            algo_trading_baton, risk_management_baton,
            cloud_infra_baton, monitoring_baton,
            payment_api_baton, payment_security_baton, payment_team_lead_baton, payment_team_lead_baton_2,
            trading_risk_baton, trading_ml_baton, trading_team_lead_baton,
            infra_security_baton, infra_monitoring_baton, infra_team_lead_baton,
            payment_fraud_baton, trading_backtest_baton, infra_container_baton,
            payment_mobile_baton, trading_compliance_baton, infra_backup_baton,
            *workflow_expansion_batons,
        ]

        canonical_statuses = [
            "enrich_ticket",
            "in_progress",
            "done",
            "handover_pending_approval",
        ]

        person_name_by_id = {
            payment_engineer_1.id: payment_engineer_1.name,
            payment_engineer_2.id: payment_engineer_2.name,
            payment_engineer_3.id: payment_engineer_3.name,
            payment_engineer_4.id: payment_engineer_4.name,
            payment_team_lead.id: payment_team_lead.name,
            payment_resilience_manager.id: payment_resilience_manager.name,
            trading_engineer_1.id: trading_engineer_1.name,
            trading_engineer_2.id: trading_engineer_2.name,
            trading_engineer_3.id: trading_engineer_3.name,
            trading_engineer_4.id: trading_engineer_4.name,
            trading_team_lead.id: trading_team_lead.name,
            infra_engineer_1.id: infra_engineer_1.name,
            infra_engineer_2.id: infra_engineer_2.name,
            infra_engineer_3.id: infra_engineer_3.name,
            infra_engineer_4.id: infra_engineer_4.name,
            infra_team_lead.id: infra_team_lead.name,
        }

        project_team_defaults = {
            payment_aws_project.id: [payment_engineer_1.id, payment_engineer_2.id, payment_team_lead.id],
            payments_legacy_migration.id: [payment_engineer_2.id, payment_engineer_4.id, payment_team_lead.id],
            algorithmic_trading_project.id: [trading_engineer_1.id, trading_engineer_3.id, trading_team_lead.id],
            risk_management_project.id: [trading_engineer_2.id, trading_engineer_4.id, trading_team_lead.id],
            cloud_infrastructure_project.id: [infra_engineer_1.id, infra_engineer_2.id, infra_team_lead.id],
            monitoring_systems_project.id: [infra_engineer_3.id, infra_engineer_4.id, infra_team_lead.id],
        }

        project_out_of_office_defaults = {
            payment_aws_project.id: [payment_engineer_3.id],
            payments_legacy_migration.id: [payment_engineer_3.id],
            algorithmic_trading_project.id: [trading_engineer_2.id, trading_engineer_4.id],
            risk_management_project.id: [trading_engineer_2.id, trading_engineer_4.id],
            cloud_infrastructure_project.id: [infra_engineer_3.id],
            monitoring_systems_project.id: [infra_engineer_3.id],
        }

        base_date = datetime(2026, 4, 1, tzinfo=timezone.utc)

        enrich_like_statuses = frozenset({"enrich_ticket"})

        for i, baton in enumerate(all_batons):
            baton.baton_status = canonical_statuses[i % len(canonical_statuses)]

            if baton.baton_status == "handover_pending_approval":
                ooo_candidates = project_out_of_office_defaults.get(baton.project_id, [])
                if ooo_candidates:
                    baton.owner_id = ooo_candidates[i % len(ooo_candidates)]

            is_imported_jira = baton.baton_status in enrich_like_statuses
            if is_imported_jira:
                # Only fields you would see on a raw Jira issue before Relay enrichment.
                baton.lifecycle_stage = "imported_ticket"
                # Jira issues always have an assignee — use the project’s primary engineer (not OOO test IDs).
                _roster = project_team_defaults.get(baton.project_id, [])
                if _roster:
                    baton.owner_id = _roster[0]
                baton.title = baton.title[:120]
                baton.detailed_context = None
                baton.implementation_state = None
                baton.dependencies = None
                baton.related_systems = None
                baton.repo_link = None
                baton.branch_name = None
                baton.troubleshooting_notes = None
                baton.reconstruction_time = None
                baton.successor_ids = []

            # Ensure successor list exists, excludes current owner, and has deterministic ordering.
            successor_ids = list(dict.fromkeys((baton.successor_ids or [])))
            successor_ids = [sid for sid in successor_ids if sid != baton.owner_id]
            if not is_imported_jira:
                if not successor_ids:
                    fallback = [pid for pid in project_team_defaults.get(baton.project_id, []) if pid != baton.owner_id]
                    successor_ids = fallback[:2]
            baton.successor_ids = successor_ids

            created_at = base_date.replace(day=((i % 20) + 1))
            updated_at = created_at.replace(day=min(28, created_at.day + 2))
            baton.created_at = created_at
            baton.updated_at = updated_at

            author_name = person_name_by_id.get(baton.owner_id, "Software Engineer")
            if is_imported_jira:
                baton.daily_logs = []
            else:
                baton.daily_logs = [
                    {
                        "date": created_at.date().isoformat(),
                        "note": f"Seeded handover context prepared for {baton.title}.",
                        "author": author_name,
                    },
                    {
                        "date": updated_at.date().isoformat(),
                        "note": f"Workflow status set to {baton.baton_status}.",
                        "author": author_name,
                    },
                ]

            if i % 3 == 0 and baton.successor_ids:
                next_owner_id = baton.successor_ids[0]
                baton.daily_logs.append(
                    {
                        "date": updated_at.date().isoformat(),
                        "note": f"[OWNER_CHANGE] {author_name} -> {person_name_by_id.get(next_owner_id, f'User {next_owner_id}')}",
                    }
                )

            if is_imported_jira:
                baton.additional_resources = []
            else:
                if baton.reconstruction_time is None:
                    baton.reconstruction_time = 30 + (i % 6) * 45
                baton.additional_resources = [
                    {
                        "type": "runbook",
                        "title": f"{baton.title} Runbook",
                        "url": f"https://github.com/example/docs/runbooks/{baton.id or i + 1}",
                    },
                    {
                        "type": "architecture_diagram",
                        "title": f"{baton.title} Architecture",
                        "url": f"https://lucid.app/lucidchart/baton-{i + 1}",
                    },
                ]

        db.add_all(all_batons)
        db.commit()

        print("Database seeded successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_db()