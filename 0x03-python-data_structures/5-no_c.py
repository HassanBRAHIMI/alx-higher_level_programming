#!/usr/bin/pyhton3
def no_c(my_string):
    string_len = len(my_string)
    new_string = ""
    i = 0
    while (i < string_len):
        if (my_string[i] != 'c' and my_string[i] != 'C'):
            new_string = new_string + my_string[i]
        i += 1
    return new_string
