# Given an array A your task is to tell at which position the equilibrium first occurs in the array.
# Equilibrium position in an array is a position such that the sum of elements below it is equal to the sum of elements after it.

arr = [1,3,5,1,1,1,1]
size = len(arr)

def equi_position(arr, size):
    sum_left = 0
    sum_right = 0
    equi_point = 1

    for i in range(size):
        if sum(arr[:equi_point]) == sum(arr[equi_point+1:]):
            print(f"The equi is at position: {equi_point+1} and value: {arr[equi_point]}")
            break
        else:
            equi_point += 1

print(f"Given array: {arr}")
equi_position(arr, size)
