mat = [[1, 2, 3, 20],
        [5, 6, 20, 25],
        [1, 3, 5, 6],
        [6, 7, 8, 15]]


def unique_elements(mat):
    no_of_rows = len(mat)
    no_of_columns = len(mat[0])

    unique_elements = []
    non_unique_elements = []

    for i in range(no_of_rows):
        for j in range(no_of_columns):
            if mat[i][j] not in unique_elements:
                unique_elements.append(mat[i][j])
            else:
                non_unique_elements.append(mat[i][j])
    print("Unique elements in given MX = {}".format(unique_elements))
    print("Non-Unique elements in given MX = {}".format(non_unique_elements))
    unique_elements.sort()
    print("Unique elements sorted in given MX = {}".format(unique_elements))


unique_elements(mat)