# FIrst sort and the merge
# Time Complexity : O (nlogn + mlogm + (n + m))
# Space Complexity : O ( (n + m) )

arr1 = [2,6,1,4]
arr2 = [5,3,7,8]
arr1_len = len(arr1)
arr2_len = len(arr2)
final_arr = [0 for i in range(arr1_len+arr2_len)]

def merge_and_sort(arr1, arr2, final_arr, arr1_len, arr2_len):
    # sort function in python: Time Complexity = O(nlogn)
    arr1.sort()
    arr2.sort()
    i,j,k = 0,0,0
    while i < arr1_len and j < arr2_len:
        if arr1[i] <= arr2[j]:
            final_arr[k] = arr1[i]
            i += 1
            k += 1
        else:
            final_arr[k] = arr2[j]
            j += 1
            k += 1
    while i < arr1_len:
        final_arr[k] = arr1[i]
        i += 1
        k += 1

    while j < arr2_len:
        final_arr[k] = arr2[j]
        j += 1
        k += 1

merge_and_sort(arr1, arr2, final_arr, arr1_len, arr2_len)
print('Merged and Sorted array : {}'.format(final_arr))