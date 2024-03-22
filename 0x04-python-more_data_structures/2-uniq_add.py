#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    huh = []
    for i in my_list:
        if i not in huh:
            sum += i
            huh.append(i)
    return sum
