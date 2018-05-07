def countingsort(arr, expl):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(0, n):
        index = (arr[i] // expl)
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // expl)
        output[count[index % 10]-1] = arr[i]
        count[(index % 10)] -= 1
        i -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radixsort(arr):
    max1 = max(arr)
    exp = 1
    while max1/exp > 0:
        countingsort(arr, exp)
        exp *= 10


arr = [170, 450, 754, 902, 802, 241, 200, 675]
print("Given Array = {}".format(arr))
radixsort(arr)
print("Sorted Array = {}".format(arr))