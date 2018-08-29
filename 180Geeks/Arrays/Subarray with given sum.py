# Given an unsorted array of non-negative integers, find a continuous sub-array which adds to a given number.

arr = [1,2,3,7,5]
given_sum = 12
size = len(arr)

def sub_arr(arr, given_sum, size):
    curr_sum = arr[0]
    start = 0
    end = 0

    while end < size:
        if curr_sum == given_sum:
            print(f"Found given sum at start index {start} = {arr[start]} and end index {end} = {arr[end]}")

        if curr_sum <= given_sum:
            end += 1
            if end < size:
                curr_sum = curr_sum + arr[end]

        else:
            curr_sum = curr_sum - arr[start]
            start += 1

sub_arr(arr,given_sum,size)
