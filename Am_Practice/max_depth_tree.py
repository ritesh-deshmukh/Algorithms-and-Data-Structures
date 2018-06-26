class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def depth(node):
    if node is None:
        return 0
    else:
        left_depth = depth(node.left)
        right_depth = depth(node.right)

        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1

root = Node(1)
root.left = (Node(2))
root.right = (Node(3))
root.left.left = (Node(4))
root.left.right = (Node(5))

print("Max Height/Depth = {}".format(depth(root)))