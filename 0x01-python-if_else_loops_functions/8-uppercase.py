#!/usr/bin/python3
def uppercase(str):
    output = ""
    for c in str:
        if ord(c) <= ord('z') and ord(c) >= ord('a'):
            output += chr(ord(c) - 32)
        else:
            output += c
    print(output.format(str))
