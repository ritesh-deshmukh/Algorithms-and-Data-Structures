mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

n = 2


def scalarMult(mat, n):
    no_of_rows = len(mat)
    no_of_columns = len(mat[0])

    for i in range(no_of_rows):
        for j in range(no_of_columns):
            mat[i][j] *= n
    print("Scalar multiplied MX = {}".format(mat))


scalarMult(mat, n)