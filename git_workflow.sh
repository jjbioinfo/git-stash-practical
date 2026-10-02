
# Name used when creating the public GitHub repository.
REPOSITORY_NAME="git-stash-practical"
# Save the absolute path of the folder from which the script is executed.
PROJECT_DIR=$(pwd)
# Hidden folder containing prepared feature and hotfix versions of files.
# It is ignored by Git and lets the video introduce changes at the correct step.
WORKFLOW_SEED="$PROJECT_DIR/.workflow_seed"

echo "Step 1: Perform safety and tool checks"
gh auth status 

echo "Step 2: Initialize and commit the initial project"
# Create a new local Git repository whose first branch is named main.
git init -b main
# Confirm that the Git author name and email are configured. The values are not
# printed because standard output is redirected to /dev/null.
git config user.name 
git config user.email
# Stage the initial project files for the first commit. 
git add \
    .gitignore \
    README.md \
    VIDEO_SCRIPT.md \
    git_workflow.sh \
    logging_config.py \
    main.py \
    task.py \
    task_manager.py \
    test_priority.py \
    test_task_manager.py \
    validators.py
# Save the staged files as the first permanent snapshot.
git commit -m "Add initial Task Manager project"
# Verify that the original Task Manager works before demonstrating Git stash.
python test_task_manager.py

echo "Step 3: Create and push the public repository"
# Create an empty public GitHub repository from this folder and connect it to
# the local repository using the conventional remote name origin.
gh repo create "$REPOSITORY_NAME" \
    --public \
    --source=. \
    --remote=origin
# Upload main and record origin/main as its upstream tracking branch.
git push -u origin main

echo "Step 4: Begin priority development without committing"
# Create and switch to a feature branch based on the current main branch.
git switch -c feature-task-priority
# Copy prepared feature versions into the working directory. These become
# modified tracked files, but they are deliberately not committed yet.
cp "$WORKFLOW_SEED/feature/task.py" task.py
cp "$WORKFLOW_SEED/feature/task_manager.py" task_manager.py
cp "$WORKFLOW_SEED/feature/main.py" main.py
cp "$WORKFLOW_SEED/feature/test_priority.py" test_priority.py
# Show the changed files and their exact uncommitted differences.
git status
git diff

echo "Step 5: Stash the unfinished feature"
# Temporarily save the tracked staged/unstaged changes and return the working
# directory to the last commit. The message explains why the stash exists.
git stash push -m "WIP task priority feature"
# Confirm that the working directory is clean after stashing.
git status
# List all locally saved stash entries; stash@{0} is the newest entry.
git stash list
# Display the complete patch stored in only the newest stash.
git stash show --patch "stash@{0}"

echo "Step 6: Switch to main and create an urgent hotfix branch"
# Leave the paused feature, return to main, and create a separate hotfix branch.
git switch main
git switch -c hotfix-empty-task-title
# Introduce the prepared urgent fix and its updated test.
cp "$WORKFLOW_SEED/hotfix/validators.py" validators.py
cp "$WORKFLOW_SEED/hotfix/test_task_manager.py" test_task_manager.py
# Run the test before committing, then inspect the exact code changes.
python test_task_manager.py
git diff
# Stage and commit only the two hotfix files.
git add validators.py test_task_manager.py
git commit -m "Reject empty task titles"
# Upload the hotfix branch and set its upstream remote branch.
git push -u origin hotfix-empty-task-title

echo "Step 7: Merge and publish the urgent fix"
# Return to main and merge the hotfix with a visible merge commit. --no-ff
# preserves the branch boundary in the Git history.
git switch main
git merge --no-ff hotfix-empty-task-title -m "Merge urgent empty-title fix"
# Upload the updated main branch to GitHub.
git push origin main
# Safely delete only the local hotfix branch after it has been merged.
git branch -d hotfix-empty-task-title

echo "Step 8: Return to the unfinished feature"
# Switch back to the feature branch where development was paused.
git switch feature-task-priority
# Prove that the saved work still exists and inspect it again.
git stash list
git stash show --patch "stash@{0}"

echo "Step 9: Demonstrate git stash apply"
# Restore only stash@{0} to the working directory. apply does not delete the
# stash entry, so the same saved work remains available for later reuse.
git stash apply "stash@{0}"
# Show the restored file changes and prove the stash entry still exists.
git status
git stash list
echo "The changes are restored, but the stash still exists."

echo "Step 10: Restore the files so the same stash can demonstrate pop"
# Discard the currently applied working-tree changes by restoring these tracked
# files from the current commit. This is safe here because apply kept the stash.
git restore task.py task_manager.py main.py test_priority.py
# Confirm that the feature branch is clean again.
git status

echo "Step 11: Demonstrate git stash pop"
# Restore stash@{0} again and remove it from the stash list after a successful
# application. If application has conflicts, Git normally keeps the stash.
git stash pop "stash@{0}"
# Show the restored changes and confirm that the stash entry was removed.
git status
git stash list
echo "The changes are restored and the stash entry has been removed."

echo "Step 12: Complete, test, commit, and push the feature"
# Validate both the priority behavior and the complete application.
python test_priority.py
python main.py
# Stage and commit the completed feature as meaningful permanent history.
git add task.py task_manager.py main.py test_priority.py
git commit -m "Add task priority feature"
# Publish the feature branch and set its upstream branch on GitHub.
git push -u origin feature-task-priority

echo "Step 13: Merge the completed feature into main"
# Merge the completed feature into main with an explicit merge commit.
git switch main
git merge --no-ff feature-task-priority -m "Merge task priority feature"
# Publish the merged main branch and remove only the merged local feature branch.
git push origin main
git branch -d feature-task-priority
# Run all tests and the demonstration from the final main branch.
python test_task_manager.py
python test_priority.py
python main.py

echo "Step 14: Demonstrate git stash drop with temporary work"
# Append a temporary uncommitted line so there is new work to stash.
printf '\nTemporary documentation experiment.\n' >> README.md
# Save the temporary change in a new stash entry.
git stash push -m "Temporary documentation experiment"
# List and inspect the newest stash before deleting it.
git stash list
git stash show --patch "stash@{0}"
# Permanently remove this stash without applying its changes.
git stash drop "stash@{0}"
# Confirm that the stash is gone and the working directory is clean.
git stash list
git status

echo "Step 15: Save the public repository URL"
# Ask GitHub CLI for the connected repository URL and store the output in a
# shell variable. $(...) is command substitution.
REPOSITORY_URL=$(gh repo view --json url --jq .url)
# Write the repository URL to the assignment submission file.
printf '# Submission Link\n\n- Repository: %s\n' \
    "$REPOSITORY_URL" > SUBMISSION_LINKS.md
# Commit and publish the submission-link file on main.
git add SUBMISSION_LINKS.md
git commit -m "Add public repository link"
git push origin main

echo "Step 16: Display the final history"
# Show the clean state, all local/remote branches, and the final branch graph.
git status
git branch --all
git log --oneline --graph --all --decorate
# Print the final public repository URL for easy copying.
echo "Repository: $REPOSITORY_URL"
