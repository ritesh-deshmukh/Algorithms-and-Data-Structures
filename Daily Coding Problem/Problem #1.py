# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

def printPairs(arr, arr_size, sum):

    s = set()

    for i in range(0, arr_size):
        temp = sum - arr[i]
        if (temp >= 0 and temp in s):
            print("Pair with the given sum is", arr[i], "and", temp)
        s.add(arr[i])

A = [6, 4, 10, 2 , 8]
n = 12
printPairs(A, len(A), n)




















# list_numbers = [10, 14, 3, 1]
# k = 17
# x = 0
#
# # arr1 = []
# len_list = len(list_numbers)
# for x in range(len_list):
#     for y in range(1, len_list):
#         if int(list_numbers[x]) + int(list_numbers[y]) == k:
#             print(f"True, {list_numbers[x]} {list_numbers[y]}")
#             break
#         else:
#             print(f"False, {list_numbers[x]} {list_numbers[y]}")
