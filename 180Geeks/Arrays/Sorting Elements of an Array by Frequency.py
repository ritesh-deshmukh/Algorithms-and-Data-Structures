# Given an array of integers, sort the array according to frequency of elements.
# For example, if the input array is {2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12}, then modify the array to {3, 3, 3, 3, 2, 2, 2, 12, 12, 4, 5}.
# If frequencies of two elements are same, print them in increasing order.

arr = [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12]
size = len(arr)

def freq(size, arr):
    freq_dict = {}

    for i in range(size):
        if arr[i] not in freq_dict:
            freq_dict[arr[i]] = arr.count(arr[i])

    # print(freq_dict)
    sorted_freq_dict = sorted(freq_dict.items(), key=lambda x: x[1])[::-1]
    for key, value in sorted_freq_dict:
        print([key]*value, end=" ")
    # print(freq_dict)

freq(size,arr)