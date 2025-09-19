git commands:

git status
1. git status

👉 Shows the current status of your branch: which files are modified, staged, or untracked.
Output (example):

On branch feature/HLE
Changes not staged for commit:
  modified:   app.py
Untracked files:
  test.py
git add

👉 Adds files to the staging area (prepares them for commit).

Example:

git add app.py
git add .


git add app.py → adds one file.

git add . → adds all modified/untracked files.

==========================
git commit

👉 Saves the staged changes into Git history.

Example:

git commit -m "Fixed bug in app.py"

===================================
4. git log

👉 Shows commit history.

Example:

git log --oneline


Output:

a12c3d4 Fixed bug in app.py
b56d7e8 Added login feature

====================================
5. git checkout

👉 Switch to another branch or restore a file.

Example:

git checkout develop
git checkout -b new-feature


git checkout develop → switch to develop.

git checkout -b new-feature → create & switch to a new branch.
================================================================
6. git merge

👉 Merge one branch into another.

Example:

git checkout develop
git merge feature/HLE


Merges changes from feature/HLE into develop.
==================================================
7. git pull

👉 Fetch + merge changes from remote repository into your current branch.

Example:

git pull origin develop
===============================================
8. git push

👉 Push local commits to remote branch.

Example:

git push origin feature/HLE
===========================================
9. git fetch

👉 Download latest commits/branches from remote but does not merge automatically.

Example:

git fetch origin
=========================================
10. git diff

👉 Show what changes you made but not committed yet.

Example:

git diff
=========================================


git clone <url>

git add .

git add <filename>

git commit -m "commit messsage"

git pull

git push

git checkout -b <branchname>

git push --set-upstream origin praveencodechanges

Run git branch -r → to see remote branches

git push origin --delete <branch\_name> --> Command to delete a remote branch

git branch -d feature1 --> delete branch

git branch -D feature1 --> force delete branch

git fetch -p



git fetch → Updates your local copy of the remote repo (downloads info about new commits, branches, tags, etc. but doesn’t merge).

git fetch -p



git fetch → Updates your local copy of the remote repo (downloads info about new commits, branches, tags, etc. but doesn’t merge).



=================================================

1\. git fetch -p



git fetch → Updates your local copy of the remote repo (downloads info about new commits, branches, tags, etc. but doesn’t merge).



The -p flag means prune.



It removes references to remote branches that no longer exist in the remote repository.



Example: If someone deleted a branch in GitHub/remote, your local still shows it in git branch -r. Running git fetch -p cleans it up.



👉 Think of it as “refreshing” your local list of remote branches.



2\. git branch -r



Shows remote branches that your local Git knows about.



Example output:



origin/HEAD -> origin/main

origin/main

origin/feature-xyz

origin/bugfix-123



In short:



git fetch -p = update + clean old references.



git branch -r = see what remote branches exist.

====================================================

git branch -a
All branches → both local and remote-tracking. Example:

main (local)

feature-test (local)

remotes/origin/main (remote)

remotes/origin/feature-xyz (remote).
====================================================

git branch -r

Remote-tracking branches only (what exists in the remote repo, like GitHub). Example: origin/main, origin/feature-xyz.

Scenario:
prave@Sri\_Karthikeya MINGW64 ~/Downloads/Batch\_3 (praveencodechanges)

$ git push origin --delete feature1

To github.com:praveenkumarilla4git/Batch-3.git

&nbsp;- \[deleted]         feature1



Here I have deleted feature1
so I want to check if the feature1 is deleted or not for that i run git branch -a; after that i can see that feature1 is still present in the command output, while feature1 is still seen in the list in the remote branch


prave@Sri\_Karthikeya MINGW64 ~/Downloads/Batch\_3 (praveencodechanges)

$ git branch -a

&nbsp; feature1

&nbsp; main

\* praveencodechanges

&nbsp; remotes/origin/HEAD -> origin/main

&nbsp; remotes/origin/feat/addition

&nbsp; remotes/origin/feat/arunacodechange

&nbsp; remotes/origin/feat/sureshcodechange

&nbsp; remotes/origin/main

&nbsp; remotes/origin/praveencodechanges



To fix this issue, we need to understand that issue is not there but why we are seeing the featrue1 in the list?
reason: This is just a stale reference in your local system, not the real remote branch.
then how to clean up:
Run the git bash command --> git fetch -p then check running git branch -a

