class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def traverse(Node):

    print(f"{Node.data}", end=" ")

    if Node.left is not None:
        traverse(Node.left)

    if Node.right is not None:
        traverse(Node.right)


root = Node("1")
root.left = Node("2")
root.left.left = Node("4")
root.left.right = Node("5")
root.right = Node("3")
# root.right.left = Node("E")
# root.right.right = Node("F")

traverse(root)