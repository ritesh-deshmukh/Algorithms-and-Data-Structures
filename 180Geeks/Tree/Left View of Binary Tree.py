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

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)

    def preorder(self):
        if self.left:
            self.left.preorder()
        print(self.data)
        # if self.right:
        #     self.right.preorder()


bst = Node(4)
bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.insert(6)
bst.insert(5)

bst.preorder()
