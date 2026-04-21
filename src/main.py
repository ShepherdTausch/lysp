import os, sys
from datetime import datetime

def sort_helper(entry):
    entry_lower = entry.name.lower()
    if entry.is_dir():
        return (0, entry_lower) # is a dir, higher priority
    else:
        return (1, entry_lower) # not a dir, lower priority

def lsdir():
    output = sorted(os.scandir("."), key=sort_helper)
    for entry in output:
        stat = entry.stat()
        if entry.is_dir():
            print(f"dir: {entry.name}")
        else:
            print(f"entry: {entry.name}")

def main():
    lsdir()

if __name__ == "__main__":
    main()
