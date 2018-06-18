class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def stack_size(self):
        return len(self.stack)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack size => {}\n".format(stack.stack_size()))
print("Popped item => {}\n".format(stack.pop()))
print("Popped item => {}\n".format(stack.pop()))
stack.push(4)
stack.push(5)
print("Stack size => {}\n".format(stack.stack_size()))
print("{}".format(stack.peek()))
