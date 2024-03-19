def print_matrix_integer(matrix=[[]]):
    if matrix:
        for rows in matrix:
            for columns in rows:
                if rows[-1] != columns:
                    print(columns, end=" ")
                else:
                    print(columns, end="")
            print()
