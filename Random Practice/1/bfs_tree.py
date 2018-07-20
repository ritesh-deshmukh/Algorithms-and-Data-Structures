class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bfs(Node):
    if Node is None:
        return

    queue = []

    queue.append(Node)

    while len(queue) > 0:
        print(queue[0].data, end=" ")
        root = queue.pop(0)

        if root.left is not None:
            queue.append(root.left)

        if root.right is not None:
            queue.append(root.right)


root = Node("1")
root.left = Node("2")
root.right = Node("3")
root.left.left = Node("4")
root.left.right = Node("5")


bfs(root)
