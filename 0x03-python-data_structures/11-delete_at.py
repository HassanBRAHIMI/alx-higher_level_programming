#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not (idx < 0 or idx > len(my_list) - 1):
        while (idx < len(my_list) - 1):
            my_list[idx] = my_list[idx + 1]
            idx += 1
        del (my_list[idx])
    return my_list
