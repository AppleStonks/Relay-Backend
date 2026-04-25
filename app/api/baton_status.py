from __future__ import annotations

CANONICAL_BATON_STATUSES = {
    "enrich_ticket",
    "in_progress",
    "awaiting_handover",
    "done",
    "handover_pending_approval",
    "handover_declined_enrich_ticket",
    "handover_declined_in_progress",
    "handover_declined_awaiting_handover",
}


def normalize_baton_status(raw: str | None) -> str:
    value = (raw or "").strip().lower().replace("-", "_").replace(" ", "_")
    if value in {"completed", "complete"}:
        return "done"
    if value in {"enrich", "enrichbaton", "enrich_baton"}:
        return "enrich_ticket"
    if value in {"waiting_to_be_accepted"}:
        return "awaiting_handover"
    if value in {"handover_declined_enrich"}:
        return "handover_declined_enrich_ticket"
    if value in CANONICAL_BATON_STATUSES:
        return value
    # hard migration fallback
    return "in_progress"
