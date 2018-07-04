def arrMin(arr, n):
    minn = arr[0]
    for i in range(n-1,0,-1):
        minn = minimum(minn, arr[i])

    return minn

def minimum(x,y):
    c = 0
    while x > 0 and y > 0:
        x = x-1
        y = y-1
        c = c+1

    return c

arr = [2,5,1,8,4]
print(arrMin(arr, len(arr)))

def min2(arr):
    minn = arr[0]
    for i in arr:
        if i < minn:
            minn = i
    return minn

arr = [8,4,7,2,6]
print(min2(arr))