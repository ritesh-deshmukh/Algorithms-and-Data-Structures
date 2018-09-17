# Level order traversal of a tree is breadth first traversal for the tree.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def levelOrderTraverse(self, root):
        if not root:
            return
        queue = []
        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.data, end=" ")
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

root.levelOrderTraverse(root)