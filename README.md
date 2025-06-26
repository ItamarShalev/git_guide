# Git Configuration Commands

Here are some useful commands to configure Git globally:

```sh
# Set your user information
git config --global user.name "Itamar Shalev"
git config --global user.email "itamar@example.com"

# Use rebase on pull by default
git config --global pull.rebase true

# Set your preferred editor (Visual Studio Code)
git config --global core.editor "code --wait"
# Alternative: Notepad++
# git config --global core.editor "'C:/Program Files/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"

# Disable GUI garbage collection warnings
git config --global gui.gcwarning false

# Configure Visual Studio Code as merge and diff tool
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd "code --wait --merge \$REMOTE \$LOCAL \$BASE \$MERGED"

git config --global diff.tool vscode
git config --global difftool.vscode.cmd "code --wait --diff \$LOCAL \$REMOTE"

# Store credentials
git config --global credential.helper store
```


# Set ssh key

```sh
# Generate a new SSH key
ssh-keygen -f ~/.ssh/custom_key
# Print the public key (which need to add to GitHub)
cat ~/.ssh/custom_key.pub
```


# Summary commands and first lesson

```sh
# Create new git repository
git init

# Import existing repository
git clone <repository-url>

# Add all files to staging area

# Understand what is . what is -u and what is --all
git add -u
git add --all
git add .

# Commit changes with a message
git commit -s

# Push changes to the remote repository
git push

# Pull changes from the remote repository
git pull origin main

# Check git status
git status

# Git diff 
git diff

# Show commit history (already committed)
git show

# Reset history
git reset --hard HEAD~1
# Mixes (changes in the working directory)
git reset HEAD~1

# Restore a file to the last committed state
git restore <file>

# Fetch changes from the remote repository without merging
git fetch

# Create a new branch (without switching to it)
git branch <new-branch-name>

# Create a new branch (with switching to it)
git checkout -b <new-branch-name>

# Switch to an existing branch
git checkout <branch-name>

# How to get help
git -h
git --help
git <command> -h # For example: git stauts -h
git <command> --help # For example: git status --help
# Using tldr tool
tldr git add

# Install tldr:
1. Install python.
2. install tldr using pip: pip install tldr
3. Update tldr pages: tldr -u


# Understand the files stages.
Untracked #files: Files that are not in the staging area.
Staged #files: Files that are in the staging area, ready to be committed.
Tracked #files: Files that are already committed to the repository.
Ignored #files: Files that are not tracked by Git, usually specified in .gitignore.

# Reference to commit:
branch
sha1
short sha1
tag
relative (HEAD~3 / HEAD^)

# Ideas
Repository (repo) # A collection of files and their history.
Commit # A snapshot of the repository at a specific point in time.
Branch # A separate line of development in the repository.
Merge # Combining changes from different branches.
Conflict (Or merge conflict) # When changes from different branches cannot be automatically merged.
Remote # A version of the repository hosted on a server (e.g., GitHub).
Remote repository # A remote repository is a version of your project that is hosted on the internet or another network.
origin # The default alias (like a nickname) for the remote repository you cloned from.
staging area # A place where you prepare files before committing them to the repository.
The diff between git and github
Patch # A file that contains differences between two versions of a file or a set of files.

# Just take a look what is:
ssh
https
token

# Learn more about these git configurations files
# Global and local git configurations
.gitignore
.gitattributes
.gitconfig




# bash commands (terminal commands in git bash)
cd <directory>  # Change directory (like entering a folder)
ls -la # List files in the current directory (with details)
pwd # Print the current working directory
rm -rf <directory>  # Remove a directory and its contents
mkdir <directory>  # Create a new directory
touch <file>  # Create a new file
cat <file>  # Display the contents of a file



# Understand the differences between configs files
toml
json
yaml
xml


# EOL (End of Line) settings
CRLF
CR
LF
