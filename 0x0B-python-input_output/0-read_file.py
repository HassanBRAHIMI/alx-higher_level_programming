#!/usr/bin/python3
""" a simple module"""


def read_file(filename=""):
    """a function that reads from a file and then writes to stdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        readed_data = f.read()
    f.close()
    print(readed_data, end="")
