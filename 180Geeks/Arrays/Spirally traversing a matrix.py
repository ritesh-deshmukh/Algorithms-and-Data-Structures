# Given a m*n matrix, traverse the matrix in spiral form.

arr = [ [1, 2, 3, 4, 5, 6],
            [7, 8, 9, 10, 11, 12],
            [13, 14, 15, 16, 17, 18] ]
no_rows = 3
no_col = 6
def spiral_traverse(arr,no_rows,no_col):
    r1 = 0
    c1 = 0

    while r1 < no_rows and c1 < no_col:
        for i in range(c1,no_col):
            print(arr[r1][i], end=" ")

        r1 += 1

        for i in range(r1,no_rows):
            print(arr[i][no_col-1], end=" ")

        no_col -= 1

        if r1 < no_rows:
            for i in range(c1-1,no_col-1,-1):
                print(arr[no_rows-1][i], end=" ")

            no_rows -= 1

        if c1 < no_col:
            for i in range(no_rows-1,r1-1,-1):
                print(arr[i][c1], end=" ")

            c1 += 1

spiral_traverse(arr,no_rows,no_rows)