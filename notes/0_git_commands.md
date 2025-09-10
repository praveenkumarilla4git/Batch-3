git commands:

git status

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

