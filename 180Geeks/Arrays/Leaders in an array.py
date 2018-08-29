# Write a program to print all the LEADERS in the array.
# An element is leader if it is greater than all the elements to its right side.
# The rightmost element is always a leader.

arr = [16,17,4,3,5,2]
size = len(arr)

def leaderfunc(arr,size):
    leader = arr[-1]
    l = []
    l.append(leader)
    # print(leader)

    for i in range(size-1,0,-1):
        if leader < arr[i]:
            # print(arr[i])
            l.append(arr[i])
            leader = arr[i]

    print(f"The leaders in the given array are: {l[::-1]}")

leaderfunc(arr,size)