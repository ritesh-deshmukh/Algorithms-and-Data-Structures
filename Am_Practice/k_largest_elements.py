arr = [2,6,1,8,4]
k = 2
# arr.sort(reverse=True)
# print(arr)

def largest(arr):
    n = len(arr)
    for i in range((n-1), 0, -1):
        for j in range(i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]
    # rev = arr[::-1]
    # print(rev)
    # arr1 = arr[::-1]
    for i in range(k):
        print(arr[i])

print(largest(arr))
