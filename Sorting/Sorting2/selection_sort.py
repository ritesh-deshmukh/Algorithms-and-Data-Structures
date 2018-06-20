# Time complexity => O(n^2)

nums = [2, 5, 3, 8, 6, 9, 4]
# nums = [-1, -3, -2, 8]
print(len(nums))


def selection_sort(nums):
    for i in range(len(nums)):
        index = i

        for j in range(i+1, len(nums)):
            if nums[j] < nums[index]:
                index = j

        if index != i:
            swap(nums, index, i)

    return nums


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


print(selection_sort(nums))