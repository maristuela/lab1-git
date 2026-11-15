"""Reporting helpers (will use stats after squash-merge)."""

def describe(values):
    return f"count={len(values)}, min={min(values)}, max={max(values)}"
