"""Initial Task Manager demonstration."""

from task import Task
from task_manager import TaskManager


def main() -> int:
    """Create and display demonstration tasks."""
    manager = TaskManager()
    manager.add_task(Task("Learn Git stash"))
    manager.add_task(Task("Record assignment video"))

    print("TASKS")
    for task in manager.list_tasks():
        print(task.display())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
