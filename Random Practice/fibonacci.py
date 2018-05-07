def fib_recursion(n):
    if n <= 1:
        return n
    else:
        return fib_recursion(n-1) + fib_recursion(n-2)


n = 5
print("Number of terms in the sequence = {}".format(n))

arr_nums = [] * n
for i in range(n):
    arr_nums.append(fib_recursion(i))
# print(arr_nums)
print("Fibonacci sequence = {}".format(arr_nums))

