# Print first n Fibonacci numbers
# Time complexity  = O(n)

def n_fib(n):
    num1 = 0
    num2 = 1

    if n < 1:
        return

    for x in range(0,n):
        print(num2, end=" ")
        next = num1 + num2
        num1 = num2
        num2 = next
n_fib(20)