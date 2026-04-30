# lysp
A python-based version of the command-line tool `ls`, designed to look like [eza](https://github.com/eza-community/eza)

### Example
``` fish
❮ lysp
drwxr-xr-x - shepherd 30 Apr 13:37 .git
drwxr-xr-x - shepherd 21 Apr 14:27 .venv
drwxr-xr-x - shepherd 28 Apr 13:46 src
-rw-r--r-- 5 Bytes shepherd 21 Apr 14:24 .python-version
-rw-r--r-- 1.0 KiB shepherd 21 Apr 14:24 LICENSE
-rw-r--r-- 199 Bytes shepherd 28 Apr 13:46 pyproject.toml
-rw-r--r-- 673 Bytes shepherd 30 Apr 13:38 README.md
-rw-r--r-- 1.7 KiB shepherd 28 Apr 13:46 uv.lock
```

### Installation
**Important!: `lysp` only works on Linux/Unix**

Clone the repo into the correct spot on your machine:
``` sh
mkdir -p ~/.local/share/bin
cd ~/.local/share/bin
git clone https://github.com/ShepherdTausch/lysp.git
```

Add an alias for the script in you shell config:
- Bash: add this to ~/.bashrc
- Zsh: add this to ~/.zshrc
- Fish: add this to ~/.config/fish/fish.config

``` text
alias lysp="python3 ~/.local/share/bin/lysp/src/main.py
```

### Contributions
Contributions are welcome in the form of pull requests and issues.
