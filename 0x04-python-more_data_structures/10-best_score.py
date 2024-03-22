#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        tada = list(a_dictionary.keys())
        score = 0
        name = ""
        for i in tada:
            if a_dictionary[i] > score:
                score = a_dictionary[i]
                name = i
        return i
