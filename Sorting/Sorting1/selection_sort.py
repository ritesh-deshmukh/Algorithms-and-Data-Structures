def selectionsort(arr):

    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [2, 5, 1, 6, 3]
print("Given Array = {}".format(arr))
selectionsort(arr)
print("Given Array = {}".format(arr))



