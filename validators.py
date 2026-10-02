"""Initial text validation used by the Task Manager."""


def require_text(value: object, field_name: str) -> str:
    """Return stripped text.

    The urgent hotfix will add the missing empty-text validation.
    """
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be text")
    return value.strip()
