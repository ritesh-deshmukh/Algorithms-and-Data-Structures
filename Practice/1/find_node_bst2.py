class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def traverse(Node):
    if Node.left is not None:
        traverse(Node.left)

    print(Node.data, end=" ")

    if Node.right is not None:
        # print("In right")
        traverse(Node.right)


def find(value, Node):
    a = Node.data
    if value == a:
        return Node
    elif value < a and Node.left != None:
        return find(value, Node.left)
    elif value > a and Node.right != None:
        return find(value, Node.right)

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)

root.right = Node(3)
# root.right.left = Node(5)
# root.right.right = Node(7)
traverse(root)
# if find(12, root):
#     print("Got it")
# else:
#     print("Not found")