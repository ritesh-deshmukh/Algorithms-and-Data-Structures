arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
arr1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
n = 4

def rotate(arr, n):
    temp = [] * n
    # count = 0
    for x in range(len(arr[:n])):
        temp.append(arr[x])

    del arr[:n]
    # print(f"Array after deletion = {arr}")

    for y in range(len(temp)):
        arr.append(temp[y])

    # print(count)
    # print(arr)
    # print(f"Temporary Array = {temp}")
    print(f"Array after shift = {arr}")

rotate(arr,n)


def shift(arr1,n):
    print(f"Other method = {arr1[n:] + arr1[:n]}")

shift(arr1,n)