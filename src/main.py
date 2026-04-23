import os, sys
import pwd
from datetime import datetime
from termcolor import colored

def sort_helper(entry):
    entry_lower = entry.name.lower()
    if entry.is_dir():
        return (0, entry_lower) # is a dir, higher priority, so 0
    else:
        return (1, entry_lower) # not a dir, lower priority, so 1

def lsdir():
    output = sorted(os.scandir("."), key=sort_helper)
    for entry in output:
        stat = entry.stat()
        if entry.is_dir():
            print(colored(f"{entry.name}/", "blue"))
        else:
            print(colored(f"{entry.name}", "white"))

def main():
    lsdir()

if __name__ == "__main__":
    main()
