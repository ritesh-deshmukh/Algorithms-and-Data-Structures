class Node:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

def mirror(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is not None and root2 is not None:
        if root1.key == root2.key:
            return (mirror(root1.leftChild, root2.rightChild) and
                    mirror(root1.rightChild, root2.leftChild))
    return False

def check(root):
    return mirror(root, root)


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.right.right = Node(3)
# root.right.left = Node(4)
# root.right.right = Node(3)

print ("1" if check(root) == True else "0")