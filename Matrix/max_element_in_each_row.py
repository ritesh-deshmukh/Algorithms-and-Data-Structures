arr = [[3, 4, 1, 8],
       [1, 4, 9, 11],
       [76, 34, 21, 1],
       [2, 1, 4, 5],
       [1, 2, 3, 4]]


def maxElement(arr):
    no_of_rows = len(arr)
    no_of_columns = len(arr[0])
    # print(no_of_rows, no_of_columns)

    for i in range(no_of_rows):
        max1 = 0
        for j in range(no_of_columns):
            if arr[i][j] > max1:
                max1 = arr[i][j]
        print("Max element in row {} = {}".format(i+1, max1))


maxElement(arr)
