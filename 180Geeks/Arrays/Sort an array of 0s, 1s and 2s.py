# Given an array containing 0s, 1s, and 2s; you need to sort the array in ascending order.

arr = [0,2,1,2,0]
size = len(arr)

def sort_arr(arr, size):
    low = 0
    mid = 0
    high = size - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1

        if arr[mid] == 1:
            mid += 1

        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

print(f"Given Array: {arr}")
print(f"Sorted Array: {sort_arr(arr, size)}")