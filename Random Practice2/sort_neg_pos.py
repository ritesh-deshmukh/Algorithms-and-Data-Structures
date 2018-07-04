# Given an array of integers, change the order of the integers so negative numbers appear first then positive numbers.
# Do not change the order of the integers.

arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6 ]
n = len(arr)

# O(n^2)
def rearrange(arr, n):
    key = 0
    j = 0

    for i in range(0,n):
        key = arr[i]
        if key > 0:
            continue

        j = i - 1
        while j>=0 and arr[j] > 0:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    return arr

print(rearrange(arr,n))

# a = [1,7,-5,9,-12,15]
# print ([x for x in a if x < 0] + [y for y in a if y >= 0])
# [-5, -12, 1, 7, 9, 15]
#
# Using extra memory
# def sort_int(arr):
#     positives = []
#     negatives = []
#
#     for num in arr:
#         if num >= 0:
#             positives.append(num)
#         else:
#             negatives.append(num)
#     return negatives+positives
#
#
# print(sort_int(arr))




# def sort_int(arr, n):
#     j = 0
#     for i in range(0, n):
#         if arr[i] < 0:
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp
#             j = j + 1
#     return arr
#
# print(sort_int(arr,n))



