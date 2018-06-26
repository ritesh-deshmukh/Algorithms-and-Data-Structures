# Given two strings str1 and str2 and below operations that can performed on str1.
# Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.
# Insert
# Remove
# Replace

# Using Dynamic programming by storing the subproblems
def str_compare(str1, str2, m, n):
    sub_problem_arr = [[0 for x in range(n+1)]for x in range(n+1)]

    for i in range(m+1):
        for j in range(n+1):

            if i == 0:
                sub_problem_arr[i][j] = j

            elif j == 0:
                sub_problem_arr[i][j] = i

            elif str1[i-1] == str2[j-1]:
                sub_problem_arr[i][j] = sub_problem_arr[i-1][j-1]

            else:
                sub_problem_arr[i][j] = 1 + min(sub_problem_arr[i][j-1],
                                                sub_problem_arr[i-1][j],
                                                sub_problem_arr[i-1][j-1])
    return sub_problem_arr[m][n]

str1 = "sunday"
str2 = "saturday"

print(str_compare(str1, str2, len(str1), len(str2)))




# without Dynamic programming O(3^n)
def edDist(str1, str2, m, n):

    if m == 0:
        return n

    if n == 0:
        return m

    if str1[m-1] == str2[n-1]:
        return edDist(str1, str2, m-1, n-1)

    return 1 + min(edDist(str1, str2, m, n-1),      # Insert
                   edDist(str1, str2, m-1, n),      # Remove
                   edDist(str1, str2, m-1, n - 1)   # Replace
                   )


str1 = "sunday"
str2 = "saturday"
print(edDist(str1, str2, len(str1), len(str2)))

