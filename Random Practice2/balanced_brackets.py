arr = [")","(", ")", "(", "(", ")", ")", ")", ")"]
# arr = '{1+[3*5+(2+1)]})'

def check_bal(arr):
    balance_dict = {'(':')', '{':'}', '[':']'}
    stack = []

    for char in arr:
        if char in balance_dict.keys():
            stack.append(char)
        elif char in balance_dict.values():
            if len(stack) == 0:
                return False
            elif balance_dict[stack[-1]] == char:
                stack.pop()
            else:
                return False
    return not len(stack)

print(check_bal(arr))