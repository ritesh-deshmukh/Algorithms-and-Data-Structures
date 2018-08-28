# palindrome
arr = "asdfds"

def palindrome(arr):
    if arr == arr[::-1]:
        return True
    else:
        palindrome(arr[1:])

print(palindrome(arr))


# remove item from string array
# arr_input = "sadksad"
# str_arr = list(arr_input)
# str_arr.remove('d')
# print(str_arr)


# Permutations of input
# arr = "asd"
# arr_input = list(arr)
# n = len(arr_input)
# left = 0
# right = n-1
# def permute(arr_input, left, right):
#     if left == right:
#         print(arr_input)
#     else:
#         for i in range(left, right+1):
#             arr_input[left], arr_input[i] = arr_input[i], arr_input[left]
#             permute(arr_input, left+1, right)
#             arr_input[left], arr_input[i] = arr_input[i], arr_input[left]
#
# print(permute(arr_input, 0, n-1))