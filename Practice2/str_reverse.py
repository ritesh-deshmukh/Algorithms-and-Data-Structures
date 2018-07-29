nums = 'hello'

# using slice and reversed
def reverse_string1(nums):
    nums = nums[::-1]
    # nums = "".join(reversed(nums))
    return nums
print(reverse_string1(nums))

# using looping
def reverse_string2(nums):
    nums2 = ""
    for num in nums:
        nums2 = num + nums2
    return nums2
print(reverse_string2(nums))

# using recursion
def reverse_string3(nums):
    if len(nums) == 0:
        return nums
    else:
        return reverse_string3(nums[1:]) + nums[0]
print(reverse_string3(nums))
