class k_closest_points(object):
    def findClosestElements(self, arr, k, x):

        if not arr or k <= 0:
            return []

        size = len(arr)
        while len(arr) > k:
            if abs(arr[0] - x) > abs(arr[-1] - x):
                arr.pop(0)
            else:
                arr.pop(-1)

        return arr


close = k_closest_points()
print(close.findClosestElements([1, 2, 3, 4, 5], 4, 3))