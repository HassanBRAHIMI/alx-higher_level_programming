#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = []
    for element in set_1:
        if element in set_2:
            common.append(element)
    common_set = set(common)
    return common_set
