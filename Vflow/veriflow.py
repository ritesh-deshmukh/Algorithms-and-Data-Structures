# find min number
arr = [121,132,2,3,4,5]

for i in range(len(arr)):
    if arr[i+1] < arr[i]:
        new_var = arr[i+1]
        break

# print(new_var)

# find min number
arr1 = [6,2,3,1,5,8,4]

least = 0

for i in range(len(arr1)):
    if arr1[i] < arr1[least]:
        least = i


# print(arr1[least])

# Find the missing number in a list
nums = [i for i in range(1,101)]
# one = 0

all_nums = nums.remove(4)
# print((nums))
for i in range(len(nums)):
    if nums[i+1] - nums[i] > 1:
        # print(i)
        break
nums.insert(i+1, nums[i]+1)
# print(nums)

# find duplicate num in a list

list_arr = [2,3,4,5,1,5,7,8]
# compare = list_arr[0]
list_arr_2 = [0] * len(list_arr)
# for i in range(0, len(list_arr)):
#     for j in range(i+1, len(list_arr)):
#         if list_arr[i] == list_arr[j]:
#             print(list_arr[i])

for i in range(0, len(list_arr)):
    if list_arr[i] not in list_arr_2:
        list_arr_2.append(list_arr[i])
    else:
        pass
        # print(list_arr[i])

# largest and smallest number in an unsorted integer array

num = list_arr[0]

for i in range(len(list_arr)):
    if list_arr[i] > num:
        num = list_arr[i]
    if list_arr[i] < num:
        pass
        # print(f"Min: {list_arr[i]}")
# print(f"Max: {num}")

# find all pairs of an integer array whose sum is equal to a given number
given_num = 5
for i in range(len(list_arr)):
    if list_arr[i] + list_arr[i+1] == given_num:
        print(list_arr[i], list_arr[i+1])
        break
    list_arr.pop(list_arr[i])
    list_arr.pop(list_arr[i+1])
    print(list_arr)
    i = 0


def printPairs(arr, arr_size, sum):
    # Create an empty hash set
    s = set()

    for i in range(0, arr_size):
        temp = sum - arr[i]
        if (temp >= 0 and temp in s):
            print("Pair with the given sum is", arr[i], "and", temp)
        s.add(arr[i])


# driver program to check the above function
A = [2,3,4,5,1,5,7,8]
n = 5
printPairs(A, len(A), n)
