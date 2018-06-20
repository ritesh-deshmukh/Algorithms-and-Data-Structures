class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Height:
    def __init__(self):
        self.height = 0


def isBalanced(root, height):
    lh = Height()
    rh = Height()

    if root is None:
        return True

    l = isBalanced(root.left, lh)
    r = isBalanced(root.right, rh)

    height.height = max(lh.height, rh.height) + 1

    if abs(lh.height - rh.height) <= 1:
        return l and r

    return False

height = Height()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.left.left.left = Node(7)
root.left.left.left.left = Node(8)

if isBalanced(root, height):
    print("Tree is balanced")
else:
    print("Not balanced")