# Given an array of integers,
# write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.



def py_triplet(arr,size):

    for i in range(size):
        arr[i] = arr[i] * arr[i]
    print(f"Squared Array: {arr}")

    arr.sort()
    print(f"Sorted squared array: {arr}")

    for i in range(size-1,1,-1):
        j = 0
        k = i - 1
        while j < k:
            if arr[j] + arr[k] == arr[i]:
                print(f"Pythagorean triplet found with {arr[j]} + {arr[k]} = {arr[i]}")
                return True
            else:
                if arr[j] + arr[k] < arr[i]:
                    j = j + 1
                else:
                    k = k - 1

    print("Pythagorean Triplet not found")
    return False


arr = [3, 1, 4, 6, 5]
size = len(arr)
print(f"Given array: {arr}")
if py_triplet(arr,size):
    # print("yes")
    pass
else:
    pass