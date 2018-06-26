def isTriplet(arr, n):
        # Square all the elemennts
        for i in range(n):
            arr[i] = arr[i] * arr[i]

        # sort array elements
        arr.sort()

        # fix one element
        # and find other two
        # i goes from n - 1 to 2
        for i in range(n-1, 1, -1):
            # start two index variables from
            # two corners of the array and
            # move them toward each other
            j = 0
            k = i - 1
            while (j < k):
                # A triplet found
                if (arr[j] + arr[k] == arr[i]):
                    return True
                else:
                    if (arr[j] + arr[k] < arr[i]):
                        j = j + 1
                    else:
                        k = k - 1
        # If we reach here, then no triplet found
        return False

    # Driver program to test above function */
arr = [3, 1, 4, 6, 5]
n = len(arr)
if(isTriplet(arr, n)):
    print("Yes")
else:
    print("No")


# for i in range(n-1, 1, -1):
#     print(arr[i])