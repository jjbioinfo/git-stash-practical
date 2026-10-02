# Video Explanation Guide

1. Show the initial working Task Manager and clean `git status`.
2. Create `feature-task-priority` and copy in the unfinished priority changes.
3. Show the changes with `git diff`, but do not commit them.
4. Run `git stash push`, then explain `stash list` and `stash show --patch`.
5. Switch to the urgent hotfix branch, reject empty task titles, test, and commit.
6. Merge the hotfix into `main`, then return to the feature branch.
7. Run `git stash apply` and show that the files return while the stash remains.
8. Restore the working files only for demonstration, then run `git stash pop`.
   Show that the changes return and the saved stash is removed.
9. Commit and merge the completed priority feature.
10. Create another temporary stash and demonstrate `git stash drop`.
11. Explain that `apply` keeps the stash, `pop` removes it after success, and
    `drop` deletes it without restoring anything.
12. Show the final application, tests, Git history, and public GitHub repository.
