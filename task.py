"""Initial Task model."""

from validators import require_text


class Task:
    """Represent a task with a title and completion status."""

    def __init__(self, title: str) -> None:
        self.title = require_text(title, "title")
        self.completed = False

    def mark_completed(self) -> None:
        """Mark this task as completed."""
        self.completed = True

    def display(self) -> str:
        """Return a readable task line."""
        status = "Done" if self.completed else "Pending"
        return f"[{status}] {self.title}"
