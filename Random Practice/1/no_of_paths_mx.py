def test(m,n):
    arr = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(m):
        arr[i][0] = 1

    for j in range(n):
        arr[0][j] = 1

    for i in range(1, m):
        for j in range(n):
            arr[i][j] = arr[i-1][j] + arr[i][j-1]
    print(arr)
    return arr[m-1][n-1]

    # print(arr, end=" ")

m = 3
n = 3
print(test(m,n))

# def no_of_paths(m, n):
#     if m == 1 or n == 1:
#         return 1
#
#     return no_of_paths(m-1, n) + no_of_paths(m, n-1)
#
#
# m = 3
# n = 3
#
# print(no_of_paths(m,n))



