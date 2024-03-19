def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for columns in rows:
            if rows[-1] != columns:
                print("{:d}".format(columns), end=" ")
            else:
                print("{:d}".format(columns), end="")
        print()
