def heapsort(arr):

    def heapify(arr, size):
        p = (size//2) - 1
        while p >= 0:
            siftdown(arr, p, size)
            p -= 1

    def siftdown(arr, i, size):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left <= size - 1 and arr[left] > arr[i]:
            largest = left
        if right <= size - 1 and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            swap(arr, i, largest)
            siftdown(arr, largest, size)

    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    size = len(arr)
    heapify(arr, size)
    end = size - 1
    while end > 0:
        swap(arr, 0, end)
        siftdown(arr, 0, end)
        end -= 1


arr = [8, 3, 9, 1, 6, 2, 5, 4]
print("Given Array = {}".format(arr))
heapsort(arr)
print("Sorted Array = {}".format(arr))

