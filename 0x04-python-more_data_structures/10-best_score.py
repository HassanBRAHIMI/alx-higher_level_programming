#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        score = 0
        name = ""
        tada = list(a_dictionary.keys())
        for i in tada:
            if a_dictionary[i] > score:
                score = a_dictionary[i]
                name = i
        return i
