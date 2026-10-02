"""Initial Task Manager tests."""

from task import Task
from task_manager import TaskManager


def test_add_and_list_tasks() -> None:
    manager = TaskManager()
    task = Task("Learn Git")
    manager.add_task(task)
    assert manager.list_tasks() == (task,)


def test_complete_task() -> None:
    task = Task("Record video")
    task.mark_completed()
    assert task.completed is True
    assert task.display() == "[Done] Record video"


def run_tests() -> int:
    """Run all test groups and return the failure count."""
    tests = [test_add_and_list_tasks, test_complete_task]
    failures = 0
    for test in tests:
        try:
            test()
            print(f"PASS: {test.__name__}")
        except Exception as error:
            failures += 1
            print(f"FAIL: {test.__name__}: {error}")
    print(f"Ran {len(tests)} test groups; failures={failures}")
    return failures


if __name__ == "__main__":
    raise SystemExit(run_tests())
