def diff(numbers, k):
    n = len(numbers)
    count = 0
    numbers = sorted(numbers)

    a = 0
    b = 0
    while b < n:
        if numbers[b] - numbers[a] == k:
            count += 1
            a += 1
            b += 1
        elif numbers[b] - numbers[a] > k:
            a += 1
        else:
            b += 1
    return count

numbers = [8, 12, 16, 4, 0, 20]
k = 4
print(diff(numbers,k))