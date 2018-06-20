# Naive solution

# def num_ways_X(n):
#     if n == 0:
#         return 1
#     total = 0
#
#     for i in {1, 3, 5}:
#         if n - 1 >= 0:
#             total += num_ways_X(n - i)
#     return total



# Better solution

# A program to count the number of ways to reach n'th stair

# Recursive function used by countWays
def countWaysUtil(n, m):
    res = [0 for x in range(n)]  # Creates list res witth all elements 0
    res[0], res[1] = 1, 1

    for i in range(2, n):
        j = 1
        while j <= m and j <= i:
            res[i] = res[i] + res[i - j]
            j = j + 1
    return res[n - 1]


# Returns number of ways to reach s'th stair
# A program to count the number of ways to reach n'th stair

# Recursive function used by countWays
def countWaysUtil(n, m):
    res = [0 for x in range(n)]  # Creates list res witth all elements 0
    res[0], res[1] = 1, 1

    for i in range(2, n):
        j = 1
        while j <= m and j <= i:
            res[i] = res[i] + res[i - j]
            j = j + 1
    return res[n - 1]


# Returns number of ways to reach s'th stair
def countWays(s, m):
    return countWaysUtil(s + 1, m)


# Driver Program
s, m = 4, 2
print("Nmber of ways =", countWays(s, m))