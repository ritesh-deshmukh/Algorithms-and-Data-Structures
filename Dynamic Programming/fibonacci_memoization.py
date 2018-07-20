# Fibonacci without memoizations i.e. using only recursion, time complexity => O(2^n)
# Fibonacci using memoization, time complexity => O(n)
# Storing result in an array


def fib(n, memo):
    if memo[n] is not None:
        return memo[n]

    if n == 1 or n == 0:
        result = 1
    else:
        result = fib(n-1, memo) + fib(n-2, memo)
    memo[n] = result
    # print(memo)
    return result


n = 6
m = n+1
memo = [None] * m
print(fib(n-1, memo))
