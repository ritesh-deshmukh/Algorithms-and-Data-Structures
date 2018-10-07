# nth fibonacci number


def get_fib(n, new):
    first_n = new
    new_old = 1
    for i in range(n):
        if i == 0:
            current = first_n
        elif i == 1:
            current = new_old
        else:
            current = new_old + first_n
            first_n = new_old
            new_old = current
    return current

print(get_fib(6,1))