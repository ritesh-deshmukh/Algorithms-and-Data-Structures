# Given an array of n positive integers.
# Write a program to find the sum of maximum sum subsequence of the given array,
# such that the integers in the subsequence are sorted in increasing order.

arr = [1,101,2,3,100,4,5]
size = len(arr)

def max_sum(arr, size):
    max = 0
    max_arr = [0 for x in range(size)]

    for i in range(size):
        max_arr[i] = arr[i]

    for i in range(size):
        for j in range(i):
            if arr[i] > arr[j] and max_arr[i] < max_arr[j] + arr[i]:
                max_arr[i] = max_arr[j] + arr[i]

    for i in range(size):
        if max < max_arr[i]:
            max = max_arr[i]

    return max


print(f"Max Sum Subsequence: {max_sum(arr,size)}")
