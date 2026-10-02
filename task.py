"""Task model with priority support."""

from numbers import Integral

from validators import require_text


class Task:
    """Represent a task with a title, priority, and completion status."""

    def __init__(self, title: str, priority: int = 3) -> None:
        self.title = require_text(title, "title")
        if isinstance(priority, bool) or not isinstance(priority, Integral):
            raise TypeError("priority must be a whole number")
        if not 1 <= priority <= 5:
            raise ValueError("priority must be between 1 and 5")
        self.priority = int(priority)
        self.completed = False

    def mark_completed(self) -> None:
        """Mark this task as completed."""
        self.completed = True

    def display(self) -> str:
        """Return a readable task line."""
        status = "Done" if self.completed else "Pending"
        return f"[{status}] {self.title}"

