# Function to print element and next greater element pair for all elements of list


def nxt_grt_elem(arr):
    for i in range(0, len(arr), 1):

        next = -1
        for j in range(i + 1, len(arr), 1):
            if arr[i] < arr[j]:
                next = arr[j]
                break

        print(str(arr[i]) + " -- " + str(next))


arr = [11, 13, 21, 3]
nxt_grt_elem(arr)