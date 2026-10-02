"""Task Manager operations with priority ordering."""

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
        logger.info(
            f"Task added: title={task.title!r}, priority={task.priority}"
        )

    def list_tasks(self) -> tuple[Task, ...]:
        """Return tasks in insertion order."""
        return tuple(self._tasks)

    def list_tasks_by_priority(self) -> tuple[Task, ...]:
        """Return tasks from highest priority (1) to lowest priority (5)."""
        return tuple(sorted(self._tasks, key=lambda task: task.priority))

