# Given two array A1[] and A2[],
# sort A1 in such a way that the relative order among the elements will be same as those  in A2.
# For the elements not present in A2. Append them at last in sorted order.
# It is also given that the number of elements in A2[] are smaller than or equal to number of elements in A1[] and A2[] has all distinct elements.

# Input: A1[] = {2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8}
#        A2[] = {2, 1, 8, 3}
# Output: A1[] = {2, 2, 1, 1, 8, 8, 3, 5, 6, 7, 9}


arr1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
arr2 = [2, 1, 8, 3]

print(f"Given array 1: {arr1}")
print(f"Given array 2: {arr2}")

def relative_sorting(arr1,arr2):
    # answer = [] * len(arr1)
    temp = []
    for i in range(len(arr1)):
        if arr1[i] in arr2 and arr2.count(arr1[i]) < 2:
            arr2.insert(arr2.index(arr1[i]),arr1[i])
            # del arr1[i]

    for i in range(len(arr1)):
        if arr1[i] not in arr2:
            temp.append(arr1[i])

    # print(f"Temp array: {temp}")
    temp.sort()
    # print(f"Sorted temp: {temp}")
    # print(f"Original first array: {arr1}")
    # print(f"Second array after insertion: {arr2}")
    print(f"Relative sorting of Array 1 and Array 2: {arr2 + temp}")

relative_sorting(arr1,arr2)