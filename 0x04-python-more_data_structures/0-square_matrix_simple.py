#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    i = 0
    for rows in matrix:
        new_matrix.append(list(map(lambda z: z ** 2, rows)))
    return new_matrix
