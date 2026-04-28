import os, sys
import stat
import pwd
from datetime import datetime
from termcolor import colored
from humanize import naturalsize

PERM_COLORS = {
    "d": "blue",
    "r": "yellow",
    "w": "red",
    "x": "green",
    "-": "light_grey"
}

class Entry():
    def __init__(self, entry, info):
        self.is_dir = entry.is_dir()
        self.permissions = stat.filemode(info.st_mode)
        if self.is_dir:
            self.size = "-"
        else:
            self.size = naturalsize(info.st_size, binary=True)
        self.owner = pwd.getpwuid(info.st_uid).pw_name
        self.date_modified = datetime.fromtimestamp(info.st_mtime).strftime('%d %b %H:%M')
        self.name = entry.name

    def add_colors(self):
        # Permissions
        colored_letters = [colored(l, PERM_COLORS[l]) for l in self.permissions]
        letters_str = "".join(colored_letters)
        self.permissions = letters_str
        
        # Size
        if self.is_dir:
            self.size = colored("-", "light_grey")
        else:
            self.size = colored(self.size, "green")

        # Owner
        self.owner = colored(self.owner, "yellow")

        # Date Modified
        self.date_modified = colored(self.date_modified, "blue")

        # Name
        if self.is_dir:
            self.name = colored(self.name, "light_blue")
        else:
            self.name = colored(self.name, "white")

def sort_helper(entry):
    entry_lower = entry.name.lower()
    if entry.is_dir():
        return (0, entry_lower) # is a dir, higher priority, so 0
    else:
        return (1, entry_lower) # not a dir, lower priority, so 1

def lsdir():
    output = sorted(os.scandir("."), key=sort_helper)
    for item in output:
        # Get stat iterable as "info"
        info = item.stat()
        # Properties
        entry = Entry(item, info)
        # Add color
        entry.add_colors()
        
        output = f"{entry.permissions} {entry.size} {entry.owner} {entry.date_modified} {entry.name}"
        print(output)

def main():
    lsdir()

if __name__ == "__main__":
    main()
