# Given a Binary Tree, print Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side.
# Left view of following tree is 1 2 4 8
#           1
#        /     \
#      2        3
#    /     \    /    \
#   4     5   6    7
#    \
#      8

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def printTree(self, root):
        max_level = [0]
        self.printTreeutil(root, 1, max_level)

    def printTreeutil(self, root, level, max_level):
        if root is None:
            return
        if max_level[0] < level:
            print(root.data)
            max_level[0] = level
        # for left view
        self.printTreeutil(root.left, level+1, max_level)
        self.printTreeutil(root.right, level+1, max_level)
        # for right view
        # self.printTreeutil(root.right, level+1, max_level)
        # self.printTreeutil(root.left, level+1, max_level)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.right = Node(8)
root.right.left = Node(6)
root.right.right = Node(7)
root.printTree(root)