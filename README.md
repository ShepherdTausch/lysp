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
**Requirements**
- Linux/Unix system
- [uv](https://astral.sh/uv)

Fetch and install the `.whl` file
``` sh
wget https://github.com/ShepherdTausch/lysp/releases/download/v0.1.0/lysp-0.1.0-py3-none-any.whl
uv tool install lysp-0.1.0-py3-none-any.whl
# Tidy up
rm lysp-0.1.0-py3-none-any.whl
```

That's it! Use lysp with:
``` sh
lysp
```

### Contributions
Contributions are welcome in the form of pull requests and issues.

### About
Written to learn how to code. :) 
