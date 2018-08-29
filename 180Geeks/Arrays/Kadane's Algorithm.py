# Given an array containing both negative and positive integers. Find the contiguous sub-array with maximum sum.

# arr = [1,2,3]
arr = [-1,-2,-3,-4]
size = len(arr)

def max_subarray(arr, size):

    max_arr = arr[0]
    curr_max = arr[0]

    for i in range(1,size):
        curr_max = max(arr[i], curr_max + arr[i])
        max_arr = max(max_arr, curr_max)

    return max_arr

print(f"Given array: {arr}")
print(f"Sub-array with maximum sum: {max_subarray(arr,size)}")