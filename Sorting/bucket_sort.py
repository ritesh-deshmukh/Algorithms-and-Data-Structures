import math


def bucketsort(A):
    code = hashing(A)
    buckets = [list() for _ in range(code[1])]

    for i in A:
        x = re_hashing(i, code)
        buck = buckets[x]
        buck.append(i)

    for bucket in buckets:
        insertion_sort(bucket)

    ndx = 0
    # merge the buckets: O(n)
    for b in range(len(buckets)):
        for v in buckets[b]:
            A[ndx] = v
            ndx += 1


def hashing(A):
    m = A[0]
    for i in range(1, len(A)):
        if m < A[i]:
            m = A[i]
    result = [m, int(math.sqrt(len(A)))]
    return result


def re_hashing(i, code):
    return int(i / code[0] * (code[1] - 1))


def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while j >= 0 and key < A[j]:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key
    return A


A = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
bucketsort(A)
print('Sorted Array = {}'.format(A))

