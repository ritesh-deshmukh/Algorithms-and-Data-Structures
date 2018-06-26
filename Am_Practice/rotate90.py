N = 4

def rotate(mat_arr):
    for x in range(0, int(N/2)):
        for y in range(x, N-x-1):
            temp = mat_arr[x][y]
            mat_arr[x][y] = mat_arr[y][N-x-1]
            mat_arr[y][N-x-1] = mat_arr[N-x-1][N-y-1]
            mat_arr[N-x-1][N-y-1] = mat_arr[N-y-1][x]
            mat_arr[N-y-1][x] = temp

def disp_mat(mat_arr):
    for i in range(0, N):
        for j in range(0, N):
            print(mat_arr[i][j], end=" ")
        print("")

mat_arr = [[0 for x in range(N)]for y in range(N)]
# print(mat_arr)

mat_arr = [ [1, 2, 3, 4 ],
        [5, 6, 7, 8 ],
        [9, 10, 11, 12 ],
        [13, 14, 15, 16 ] ]


rotate(mat_arr)

disp_mat(mat_arr)