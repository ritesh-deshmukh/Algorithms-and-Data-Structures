# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.


arr = [30, -2, 24, -1, 11]
print(f"Given Array = {arr}")
arr.sort()
print(f"Sorted Array = {arr}")
sum1 = 0
count = 0
for x in range(len(arr)):
    if arr[x] < 0:
        count += 1
        continue
    else:
        sum1 += arr[x]

default_sum = sum(i for i in range(arr[count],arr[-1]+1))

arr.append(default_sum-sum1)



print(f"First positive Element = {arr[count]}")
print(f"Last Element = {arr[-1]}")
print(f"Sum of positive numbers = {sum1}")
print(f"Position of first positive number in the array(0,1,2...) = {count}")
print(f"Default Sum from {arr[count]} to {arr[-1]} = {default_sum}")
print(f"Missing first positive number = {default_sum-sum1}\n")
print(f"Final Array = {arr}")




# a = [0,1,3,4,5,6,7,8,9]
# first = a[1] # 1
# last = a[4]  # 5
# # print(sum(range(4)))
# x = sum(i for i in range(first,last))
# print(x)