"""Demonstrate the Task Manager priority feature."""

from task import Task
from task_manager import TaskManager


def main() -> int:
    """Create tasks and display them in priority order."""
    manager = TaskManager()
    manager.add_task(Task("Learn Git stash", priority=1))
    manager.add_task(Task("Record assignment video", priority=2))
    manager.add_task(Task("Review study notes", priority=4))

    print("TASKS BY PRIORITY")
    for task in manager.list_tasks_by_priority():
        print(f"Priority {task.priority}: {task.display()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

