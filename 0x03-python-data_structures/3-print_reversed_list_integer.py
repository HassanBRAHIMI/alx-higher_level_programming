#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    index = length - 1
    while (index >= 0):
        print("{:d}".format(my_list[index]))
        index -= 1
