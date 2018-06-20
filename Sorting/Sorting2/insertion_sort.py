# nums = [2, 5, 3, 8, 6, 9, 4]
nums = [-1, -3, -2, 8]


def insertion_sort(nums):
    for i in range(len(nums)):
        j = i

        while j > 0 and nums[j-1] > nums[j]:
            swap(nums, j, j-1)
            j = j - 1

    return nums


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


print(insertion_sort(nums))