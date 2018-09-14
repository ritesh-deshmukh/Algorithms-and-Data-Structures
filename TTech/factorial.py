def fact_recursion(n):
    if n == 1 or n == 0:
        return 1
    return n*fact_recursion(n-1)

print(f"Factorial using Recursive approach: {fact_recursion(4)}")


def fact_iterative(n):
    res = 1
    for i in range(1,n+1):
        res *= i

    return res

print(f"Factorial using Iterative approach: {fact_iterative(4)}")
