def maxDifference(a):
    n = len(a)
    maxD = a[1] - a[0]
    minD = a[0]

    for i in range(1, n):
        if (a[i] - minD > maxD):
            maxD = a[i] - minD

        if (a[i] < minD):
            minD = a[i]
    return maxD


# Driver program to test above function
a = [1, 2, 6, 80, 100]
print("MaxDimum difference is",
      maxDifference(a))




# Distinct pairs

# Complete the countPairs function below.
def countPairs(numbers, k):
    n = len(numbers)
    count = 0
    for i in range(0, n):
        for j in range(i+1, n) :
            if numbers[i] - numbers[j] == k or numbers[j] - numbers[i] == k:
                count += 1
    return count