class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def inOrder(self):
        if self.left:
            self.left.inOrder()
        print(self.data)
        if self.right:
            self.right.inOrder()

    def minValue(self, node):
        current = node
        while current.left is not None:
            current = current.left
        print(current.data)

    def maxValue(self, node):
        current = node
        while current.right is not None:
            current = current.right
        print(current.data)

root = Node(14)
root.insert(12)
root.insert(6)
root.insert(8)
root.insert(15)
root.insert(16)
root.insert(18)
print("in order")
root.inOrder()
print("Min element")
root.minValue(root)
print("Max element")
root.maxValue(root)