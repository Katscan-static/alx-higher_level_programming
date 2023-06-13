#!/usr/bin/python3
"""
    a module that deletes everything and writes new data
"""


def write_file(filename="", text=""):
    """

    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
