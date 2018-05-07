mat = [[2, 9, 1, 4, -2],
       [6, 7, 2, 11, 4],
       [4, 2, 9, 2, 4],
       [1, 9, 2, 4, 4],
       [0, 2, 4, 2, 5]]


def diagSum(mat, n):

    diagonal1_left = 0
    diagonal2_left = 0
    diagonal1_right = 0
    diagonal2_right = 0

    no_of_rows = len(mat)
    no_of_columns = len(mat[0])

    for i in range(no_of_rows):
        for j in range(no_of_columns):
            if i < (n/2):
                diagonal1_left += mat[i][j]
                diagonal2_left += mat[j][i]
            elif i > (n/2):
                diagonal1_right += mat[i][j]
                diagonal2_right += mat[j][i]

    if diagonal1_left == diagonal2_right and diagonal2_right == diagonal2_left and diagonal1_right == diagonal2_left and diagonal2_right == mat[n/2][n/2]:
        print("yes")
    else:
        print("no")


diagSum(mat, 5)
