def createStack():
    stack = []
    return stack

def size(stack):
    return len(stack)

def isEmpty(stack):
    if size(stack) == 0:
        return True

def push(stack, item):
    stack.append(item)

def pop(stack):
    if len(stack) == 0:
        return
    return stack.pop()

def reverse(given_str):
    n = len(given_str)

    # Create empty stack
    stack = createStack()

    # push all elements of given string to the stack
    for i in range(0,n,1):
        push(stack, given_str[i])

    given_str = ""

    # push all items back to the given string in a reverse order
    for i in range(0,n,1):
        given_str += pop(stack)

    return given_str

given_str = 'hello'
print("Given String is: {}".format(given_str))

print("The reversed string is: {}".format(reverse(given_str)))