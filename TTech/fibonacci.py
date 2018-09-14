# def fibR(n):
#  if n<=1:
#     return n
#  else:
#     return fibR(n-1)+fibR(n-2)
#
# # n = 5
# # for i in range(n):
# #     print(fibR(i))
# print(fibR(5))

def Fib(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a

n = 5
for i in range(n):
    print(Fib(i))