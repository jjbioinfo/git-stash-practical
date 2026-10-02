"""Task Manager tests including the empty-title hotfix."""

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


def test_empty_title_is_rejected() -> None:
    assert_raises(ValueError, Task, "")
    assert_raises(ValueError, Task, "   ")


def test_non_text_title_is_rejected() -> None:
    assert_raises(TypeError, Task, 123)


def run_tests() -> int:
    """Run all test groups and return the failure count."""
    tests = [
        test_add_and_list_tasks,
        test_complete_task,
        test_empty_title_is_rejected,
        test_non_text_title_is_rejected,
    ]
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

