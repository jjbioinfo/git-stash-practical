"""Initial Task Manager operations."""

import logging

from task import Task

logger = logging.getLogger(__name__)


class TaskManager:
    """Store tasks and provide task operations."""

    def __init__(self) -> None:
        self._tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        """Add a Task object."""
        if not isinstance(task, Task):
            raise TypeError("task must be a Task object")
        self._tasks.append(task)
        logger.info(f"Task added: title={task.title!r}")

    def list_tasks(self) -> tuple[Task, ...]:
        """Return tasks without exposing the mutable internal list."""
        return tuple(self._tasks)
