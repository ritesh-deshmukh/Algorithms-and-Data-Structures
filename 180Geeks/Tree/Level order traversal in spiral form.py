# Write a function to print spiral order traversal of a tree.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def spiralTraverse(self, root):
        if root is None:
            return
        currentLevel = []
        nextLevel = []
        currentLevel.append(root)
        ltr = False
        while len(currentLevel) > 0:
            temp = currentLevel.pop(-1)
            print(temp.data, end=" ")
            if ltr:
                if temp.left:
                    nextLevel.append(temp.left)
                if temp.right:
                    nextLevel.append(temp.right)
            else:
                if temp.right:
                    nextLevel.append(temp.right)
                if temp.left:
                    nextLevel.append(temp.left)

            if len(currentLevel) == 0:
                ltr = not ltr
                currentLevel, nextLevel = nextLevel, currentLevel


root = Node(1)
root.left = Node(2)
root.left.right = Node(6)
root.left.left = Node(7)
root.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(4)
root.spiralTraverse(root)
# root.printTree()
