My first news app
=================

Activate a virtual env and then create a new Git repository

$ git init repo

=================

Go into repo

$ cd repo

=================

Creates a file using the command line

touch (filename)

=================

Add a file for git to track (won't track files you don't add)

$ git add README.md

$ git add . # adds everything

Removes that file

git reset HEAD <file>

=================

Commit to git with a comment (tells it to queue changed and tracked files)

$ git commit -m "Commit message"

=================

Send the changed files

$ git push origin master

=================

How to check what it's watching: git status

- push sends to git
- pull grabs from git
- origin is github
- master is the main branch (in this case, master is the main)

=================

How to set aliases for commands

git config --global alias.st status

git config --global alias.po push origin


=================

.gitignore will list the files to ignore

stuff/*.* - for instance ignores everything in the directory stuff, even if you commit everything .

