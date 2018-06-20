n = 4
# Just like fibonacci
# Naive solution, more space complexity
def num_ways(n):
    if n == 1 or n == 0:
        return 1
    else:
        return num_ways(n-1) + num_ways(n-2)

print(num_ways(4))


# Better Solution to save space and time using Dynamic Programming - Bottom Up
def num_ways_bottom_up(n):
    if n == 0 or n == 1:
        return n
    x = n+1
    nums = [x]
    nums[0] = 1
    nums[1] = 1

    for i in range(2, n):
        nums[i] = nums[i-1] + nums[i-2]
    return nums[n]
print(num_ways_bottom_up(4))

def staircase(n):
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b
    return a

# There's a staircase with N steps, and you can climb 1 or 2 steps at a time.
# Given N, write a function that returns the number of unique ways you can climb the staircase.
# The order of the steps matters.
#
# For example, if N is 4, then there are 5 unique ways:
#
# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X.
