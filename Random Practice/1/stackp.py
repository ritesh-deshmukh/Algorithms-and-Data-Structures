def push(arr, data):
    arr.append(data)


def pop(arr):
    popped_item = arr[-1]
    del arr[-1]
    return popped_item


def peek(arr):
    peeked_item = arr[-1]
    return peeked_item


def stack_size(arr):
    return len(arr)


def isEmpty(arr):
    return arr == []


arr = []
print(isEmpty(arr))
push(arr, 2)
print(isEmpty(arr))
push(arr, 3)
push(arr, 4)
print(stack_size(arr), "\n")
print(peek(arr), "\n")
print(pop(arr), "\n")
print(arr, "\n")
print(stack_size(arr), "\n")
print(peek(arr), "\n")
print(arr)
