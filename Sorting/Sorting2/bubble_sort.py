# nums = [2, 5, 3, 8, 6, 9, 4]
nums = [-1, -3, -2, 8]


def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(0, len(nums) - 1 - i):
            if nums[j] > nums[j+1]:
                swap(nums, j, j+1)
    return nums


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


print(bubble_sort(nums))

# Time complexity => O(n^2)
