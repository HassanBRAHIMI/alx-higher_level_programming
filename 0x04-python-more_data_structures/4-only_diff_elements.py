#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = []
    for element in set_1:
        if element not in set_2:
            diff.append(element)
    for tada in set_2:
        if tada not in set_1:
            diff.append(tada)
    diff_set = set(diff)
    return diff_set
