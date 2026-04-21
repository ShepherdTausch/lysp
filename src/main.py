import os, sys
from datetime import datetime

def lsdir():
    output = sorted(os.scandir("."), key=lambda f: f.name.lower())
    for file in output:
        stat = file.stat()
        if file.is_dir():
            print(f"dir: {file.name}")
        else:
            print(f"file: {file.name}")

def main():
    lsdir()

if __name__ == "__main__":
    main()
