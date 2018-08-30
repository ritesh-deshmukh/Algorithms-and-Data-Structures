# Given an array and an integer k, find the maximum for each and every contiguous subarray of size k.

arr = [1,2,3,1,4,5,2,3,6]
# arr = [8,5,10,7,9,4,15,12,90,13]
k = 3
size = len(arr)
count = 0
def max_subarray(arr,k,size,count):
    temp_arr = []*k
    initial_index = 0
    if count < size+k+2:
        for i in range(0,3):
            temp_arr.append(arr[i])
        count += 1
        print(max(temp_arr),end=" ")
        temp_arr.clear()
        del arr[initial_index]
        max_subarray(arr,k,len(arr),count)

    else:
        print("End of array")

print(f"The max of each subarray of size {k} is ")
max_subarray(arr,k,size,count)