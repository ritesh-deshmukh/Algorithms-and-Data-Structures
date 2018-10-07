# Start and end position

def findFirstAndLast(line, n, x):
    first = -1
    last = -1
    ans = []
    for i in range(0, n):
        if (x != line[i]):
            continue
        if (first == -1):
            first = i
        last = i

    if (first != -1):
        ans.append(first)
        ans.append(last)
        print(ans)
    else:
        print("Not Found")

line = '[5,7,7,8,8,10]'
import re
dum =  [int(s) for s in re.findall(r'\b\d+\b', line)]
# Driver code
# line = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
n = len(line)
x = 1
findFirstAndLast(dum, n, x)