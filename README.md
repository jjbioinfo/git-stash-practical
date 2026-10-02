# Git Stash Practical

This project uses a Python Task Manager to demonstrate how `git stash` temporarily
saves unfinished work when an urgent task interrupts feature development.

## Scenario

1. Begin implementing task priorities on `feature-task-priority`.
2. Leave the feature changes uncommitted.
3. Save the work using `git stash`.
4. Switch to `hotfix-empty-task-title` and correct urgent validation.
5. Commit and merge the hotfix into `main`.
6. Return to the feature branch and inspect the stash.
7. Demonstrate both `git stash apply` and `git stash pop`.
8. Commit and merge the finished priority feature.
9. Create a temporary stash and remove it using `git stash drop`.

## Stash commands demonstrated

| Command | Purpose |
|---|---|
| `git stash push -m "message"` | Saves tracked uncommitted changes |
| `git stash list` | Lists saved stash entries |
| `git stash show --patch` | Displays the changes stored in a stash |
| `git stash apply` | Restores changes but keeps the stash entry |
| `git stash pop` | Restores changes and removes the stash if successful |
| `git stash drop` | Deletes a stash without restoring its changes |

## Difference between apply and pop

`git stash apply` restores a stash but leaves it in `git stash list`, so it can be
used again. `git stash pop` restores a stash and removes it after a successful
application. Use `apply` when you want a safer reusable copy; use `pop` when you
want to restore the work and no longer need the saved entry.

## Initial project files

```text
8_git_stash_practical/
├── .gitignore
├── README.md
├── VIDEO_SCRIPT.md
├── git_workflow.sh
├── logging_config.py
├── main.py
├── task.py
├── task_manager.py
└── test_task_manager.py
```

The ignored `.workflow_seed/` directory contains the prepared hotfix and priority
changes. The script copies them at the appropriate points without committing the
feature before it is stashed.

## Run the initial version

```bash
python main.py
python test_task_manager.py
```

## Run the Git demonstration

Review the script, then execute it while recording:

```bash
bash git_workflow.sh
```

GitHub CLI must be installed and authenticated. The script creates a public
repository named `git-stash-practical`.

## Submission links

- Public GitHub repository: `GENERATED-AFTER-RUNNING-THE-SCRIPT`
- YouTube video: `ADD-YOUTUBE-VIDEO-URL`
