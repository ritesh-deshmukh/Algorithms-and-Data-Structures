def numberOfPaths(m, n):

    # Create a 2D table to store results of subproblems
    count = [[0 for _ in range(m)] for _ in range(n)]

    # Count of paths to reach any cell in first column is 1
    for i in range(m):
        count[i][0] = 1

    for j in range(n):
        count[0][j] = 1

    # Calculate count of paths for other cells in bottom-up manner
    for i in range(1, m):
        for j in range(n):
            count[i][j] = count[i - 1][j] + count[i][j - 1]
    return count[m - 1][n - 1]


m = 3
n = 3
print(numberOfPaths(m, n))
