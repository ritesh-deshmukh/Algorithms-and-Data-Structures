# Given an array of distinct elements, rearrange the elements of array in zig-zag fashion in O(n) time.
# The converted array should be in form a < b > c < d > e < f.
# The relative order of elements is same in the output i.e you have to iterate on the original array only.


arr = [4,3,7,8,6,2,1]
size = len(arr)

def zigzag(arr,size):
    rules = ["<",">"]
    flag = True
    for i in range(size-1):
        if flag == True:
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        else:
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        flag = bool(1-flag)
    print(f"Array in the zigzag form (a < b > c < d > e < f): {arr}")

print(f"Given array: {arr}")
zigzag(arr,size)