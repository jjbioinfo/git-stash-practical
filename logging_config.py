"""Logging configuration for the Task Manager."""

import logging
from pathlib import Path

LOG_FILE = Path(__file__).with_name("logs") / "task_manager.log"


def configure_logging() -> None:
    """Log DEBUG and higher messages to the terminal and a file."""
    LOG_FILE.parent.mkdir(exist_ok=True)
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
        ],
        force=True,
    )
