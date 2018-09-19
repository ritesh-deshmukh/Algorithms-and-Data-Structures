# Given an unsorted array of non-negative integers, find a continuous sub-array which adds to a given number.

nums = [1,2,3,7,5]
sum = 12

def subarr(nums, sum):
    len_nums = len(nums)
    for i in range(len_nums):
        current_sum= nums[i]
        j = i + 1
        while j <= len_nums:
            if current_sum == sum:
                print(f"Sum found between position {i} = {nums[i]} and position {j-1} = {nums[j-1]}")
                return 1
            if current_sum > sum or j == len_nums:
                break
            current_sum = current_sum + nums[j]
            j += 1
    print("Sum not found")

print(f"Given arr of numbers: {nums}")
print(f"Given sum: {sum}")
subarr(nums,sum)
