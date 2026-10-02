"""Tests for the task-priority feature."""

from collections.abc import Callable

from task import Task
from task_manager import TaskManager


def assert_raises(
    expected_exception: type[BaseException],
    function: Callable[..., object],
    *arguments: object,
) -> None:
    """Confirm that a call raises the expected exception."""
    try:
        function(*arguments)
    except expected_exception:
        return
    except Exception as error:
        raise AssertionError(
            f"expected {expected_exception.__name__}, got {type(error).__name__}"
        ) from error
    raise AssertionError(f"expected {expected_exception.__name__}")


def test_default_and_explicit_priority() -> None:
    default_task = Task("Default priority")
    urgent_task = Task("Urgent task", 1)
    assert default_task.priority == 3
    assert urgent_task.priority == 1


def test_priority_ordering() -> None:
    manager = TaskManager()
    low = Task("Low priority", 5)
    high = Task("High priority", 1)
    medium = Task("Medium priority", 3)
    for task in (low, high, medium):
        manager.add_task(task)
    assert manager.list_tasks_by_priority() == (high, medium, low)


def test_invalid_priorities() -> None:
    assert_raises(TypeError, Task, "Boolean priority", True)
    assert_raises(TypeError, Task, "Decimal priority", 1.5)
    assert_raises(ValueError, Task, "Priority too small", 0)
    assert_raises(ValueError, Task, "Priority too large", 6)


def run_tests() -> int:
    """Run all priority test groups and return the failure count."""
    tests = [
        test_default_and_explicit_priority,
        test_priority_ordering,
        test_invalid_priorities,
    ]
    failures = 0
    for test in tests:
        try:
            test()
            print(f"PASS: {test.__name__}")
        except Exception as error:
            failures += 1
            print(f"FAIL: {test.__name__}: {error}")
    print(f"Ran {len(tests)} priority test groups; failures={failures}")
    return failures


if __name__ == "__main__":
    raise SystemExit(run_tests())

