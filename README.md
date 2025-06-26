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
