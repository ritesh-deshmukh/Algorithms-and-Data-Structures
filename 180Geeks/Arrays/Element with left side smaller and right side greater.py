# Given an unsorted array of size N.
# Find the first element in array such that all of its left elements are smaller and all right elements to it are greater than it.

arr = [4,2,5,7]
size = len(arr)

def mid(arr, size):
    temp = 0
    for i in range(0,size):
        flag = 0

        for j in range(0,i):
            if arr[j] >= arr[i]:
                flag = 1
                break

        for j in range(i+1,size):
            if arr[j] <= arr[i]:
                flag = 1
                break

        if flag == 0:
            print(f"Midpoint in the array is {arr[i]} at position {i+1}")
            return

    print("Midpoint not found")
    return

print(f"Given array: {arr}")
mid(arr,size)