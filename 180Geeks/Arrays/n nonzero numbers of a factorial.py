def six_ending_digits(n):
    x = fact(n)
    y = str(x)[::-1]
    ans = []
    for i in range(0,6):
        ans.append(int(str(int(y))[i]))

    # z = str(int(y))[0]
    # w = int(z)
    print(ans)


def fact(n):
    if n==0:
            return 1
    else :
            return n*fact(n-1)


six_ending_digits(44)