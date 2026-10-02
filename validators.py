"""Text validation used by the Task Manager."""


def require_text(value: object, field_name: str) -> str:
    """Return non-empty text after removing surrounding spaces."""
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be text")
    cleaned_value = value.strip()
    if not cleaned_value:
        raise ValueError(f"{field_name} cannot be empty")
    return cleaned_value

