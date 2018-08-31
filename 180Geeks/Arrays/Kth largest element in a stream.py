# Given an input stream of n integers the task is to insert integers to stream and print the kth largest element in the stream at each insertion.
#
# Input:
# stream[] = {10, 20, 11, 70, 50, 40, 100, 5, ...}
# k = 3#
# Output:    {-1,   -1, 10, 11, 20, 40, 50,  50, ...}


arr = [1, 23, 12, 9, 30, 2, 50]
k = 3

def k_largest_elem(arr,k):
    arr.sort(reverse=True)
    for i in range(k):
        print(arr[i], end=" ")

k_largest_elem(arr,k)