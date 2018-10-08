import copy

li1 = [1, 2, [3, 5], 4]

li2 = copy.deepcopy(li1)
# print(li1)

print("\r")

li2[2][0] = 7

# print(li1)

x = [1,2,3,4,[12,41],6]
y = copy.copy(x)
y = copy.deepcopy(x)

# y = x[:]
print(x)
y[4][0] = 10
print(x)
# print(y)