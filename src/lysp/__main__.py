import os


def main():
    [print(*x, sep="\n") for x in next(os.walk("."))[1:2]]
