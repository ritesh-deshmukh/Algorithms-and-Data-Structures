class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None

class LLTREE:
    def connect(self, root):
        if not root:
            return
        current_level = [root]

        # state = False
        while current_level:
            next_level = []
            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            for i in range(len(next_level) - 1):
                next_level[i].next = next_level[i+1]
            current_level = next_level

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

connect_tree = LLTREE()
connect_tree.connect(root)
print(root.data)
print(root.left.data)
print(root.left.next.data)
print(root.right.data)
print(root.right.next)
print(root.left.left.data)
print(root.left.left.next.data)