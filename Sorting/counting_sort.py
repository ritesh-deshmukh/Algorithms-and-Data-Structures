def counting_sort(array, maxvalue):
    m = maxvalue + 1
    count = [0] * m
    for a in array:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            array[i] = a
            i += 1
    return array


arr = [4, 3, 9, 6, 8, 2]
print("Given Array = {}".format(arr))
maxvalue = max(arr)
counting_sort(arr, maxvalue)
print("Sorted Array = {}".format(arr))

