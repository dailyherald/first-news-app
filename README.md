My first news app
=================

Activate a virtual env and then create a new Git repository: 
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

Removes that file

git reset HEAD <file>

=================

Commit to git with a comment (tells it to queue changed and tracked files)

$ git commit -m "First commit"

=================

Send the changed files

$ git push origin master

=================

How to check what it's watching: git status

- push sends to git
- pull grabs from git
- origin is the repo
- master is the new git branch (in this case, first-news-app at git)

=================

How to set aliases for commands

git config --global alias.st status

git config --global alias.po push origin


=================

