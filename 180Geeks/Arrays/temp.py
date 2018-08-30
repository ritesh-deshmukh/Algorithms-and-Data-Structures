# Problem Statement
# You and your friends are visiting an amusement park. Everyone wants to ride the most famous attraction, the world's slowest roller coaster. There is a minimum height and a maximum height to be allowed on the ride. Your task is to count the number of people who will be able to go on the roller coaster.
#
# Implement the method countRiders. The method has three parameters: heights, minHeight, and maxHeight. heights  is an array of integers containing the heights of the people who want to go on the ride. minHeight  is the minimum height allowed on the ride, inclusive. maxHeight  is the maximum height allowed on the ride, inclusive. The method should return the number of people able to go on the ride.
#
#
# Constraints
# heights  contains between 0 and 100 elements
# minHeight  ≤ maxHeight
# Examples
# heights  = {32, 10, 91, 40}
# minHeight  = 10
# maxHeight  = 50
# Output: 3


# heights = [32, 10, 91, 40]
# minHeight = 10
# maxHeight = 50

def count_riders(heights, minHeight, maxHeight):
    # Implement this function
    count = 0
    for i in range(len(heights)):
        if heights[i] <= maxHeight and heights[i] >= minHeight:
            count += 1

    return count

# print(count_riders(heights,minHeight,maxHeight))


if __name__ == '__main__':
    heights = [32, 10, 91, 40]
    minHeight = 10
    maxHeight = 50
    answer = count_riders(heights, minHeight, maxHeight)
    print("My answer: %s" % answer)
    print("Expected answer: %s" % 3)


# from __future__ import print_function
#
# def g_a(n):
#     return n * (n-1) // 2
#
#
# def g_b(n):
#     return (n-1) * n // 2
#
# def f(n):
#     return (g_a if n % 2 else g_b)(n)
#
# if __name__ == '__main__':
#     print(f(4))


# def add_args(one,two):
#     x1 = [two/one]
#
#     def closure():
#         three = 15
#         four = three * 2
#
#         x1[0] = 5 + four
#
#         print(x1[0], " ", end='')
#
#     closure()
#     print(x1[0])
#
# def main():
#     add_args(10,20)
# main()
#
import sys
# def main():
#     sysPrinters = {}
#     for i in range(1,4):
#         sysPrinters[i] = "printer" + str(i)
#
#         for keys in sysPrinters:
#             print(sysPrinters[keys]),
#
#         return 0
#
# main()




def main():
    tampa = "tampa"
    florida = "florida"

    tampa = tampa[3: 5] + tampa[2]
    co = florida.find(tampa[1])
    florida = tampa + florida[co: co + 1]
    print(florida)

main()