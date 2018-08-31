# The cost of a stock on each day is given in an array,
# find the max profit that you can make by buying and selling in those days.

arr = [23,13,25,29,33,19,34,45,65,67]
size = len(arr)


def max_profit(arr,size):
    temp = 0
    min_stock = min(arr)
    min_stock_place = 0
    temp = 0

    for index, item in enumerate(arr):
        if item == min_stock:
            min_stock_place = index

    i = 1
    for i in range(len(arr[min_stock_place:])+1):
        if arr[i] > min_stock and arr[i-1] < arr[i]:
            temp = arr[i]


    return temp


print(max_profit(arr,size))