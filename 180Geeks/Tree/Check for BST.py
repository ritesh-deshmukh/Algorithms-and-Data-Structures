# Given a binary tree, return true if it is BST, else false. For example, the following tree is not BST, because 11 is in left subtree of 10.
#         10
#      /     \
#    7       39
#      \
#       11

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def checkBST(self, root, min, max):
        if root == None:
            return True
        if root.data <= min or root.data >= max:
            return False
        return self.checkBST(root.left, min, root.data) and self.checkBST(root.right, root.data, max)

    def checkBSTController(self, root):
        return self.checkBST(root, -2147483648, 2147483647)

root = Node(10)
root.left = Node(7)
root.left.right = Node(11)
root.right = Node(39)

print(root.checkBSTController(root))
