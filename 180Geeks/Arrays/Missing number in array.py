# Given an array of size n-1 and given that there are numbers from 1 to n with one missing, the missing number is to be found.


# arr = [1,2,3,5]
arr = [-5,-3,-2,-1]
size = len(arr)

def missing_number(arr, size):

    missing_index = 0

    for i in range(size):
        if arr[i+1] - arr[i] > 1:
            missing_index = i
            break

    print(f"Given array: {arr}")
    # to add the missing number to the array
    arr.insert(missing_index+1, arr[missing_index]+1)

    print(f"The missing number is: {arr[missing_index]+1}")
    print(f"The missing number will be at index: {missing_index + 1}")
    print(f"The array after inserting the missing number: {arr}")


missing_number(arr,size)