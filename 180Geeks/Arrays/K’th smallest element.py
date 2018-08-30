# Given an array and a number k where k is smaller than size of array,
# the task is to find the k’th smallest element in the given array.
# It is given that all array elements are distinct.
#

arr = [7,10,4,3,20,15]
size = len(arr)
n = 3

def k_smallest_element(arr,n):
    arr.sort()
    return arr[n-1]

print(f"Given array: {arr}")
print(f"The smallest element at position: {n} in the given array is: {k_smallest_element(arr,n)}")


# class element(object):
#     def __init__(self):
#         self.stack = []
#         self.value = 0
#         self.count = 0
#
#     def push(self,value):
#         self.count += 1
#         self.stack.append(value)
#
#     def pop(self):
#         self.count -= 1
#         del self.stack[-1]
#
#     def print(self):
#         print(self.stack[::-1])
#
#
# e = element()
# e.push(1)
# e.push(2)
# e.push(3)
# e.push(4)
# e.pop()
# e.print()
