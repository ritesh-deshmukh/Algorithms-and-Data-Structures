# Given a sorted array of integers, every element appears twice except for one.
# Find that single one in linear time complexity and without using extra memory.

arr = [1,1,2,2,3,3,4,50,50,65,65]
# arr = [1,1,2,3,3]
size = len(arr)

def single(arr):
    print(f"Given array: {arr}")
    print(2*sum(set(arr)) - sum(arr))


single(arr)