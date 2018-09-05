# Given a string S, find the longest palindromic substring in S.

a = [1,2,3]
n = len(a)

def _rec(a, n):
    if len(a) == 1:
        return a[0]

    else:
        return a[0] + _rec(a[1:], n)

print(_rec(a,n))