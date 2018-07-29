# Breadth first search for Graph

class Node(object):
    def __init__(self, data):
        self.data = data
        self.adjacencyList = []
        self.visited = False


def bfs_traverse(node):
    queue = []
    queue.append(node)
    node.visited = True

    while queue:
        actualNode = queue.pop(0)
        print(f"{actualNode.data}", end=" ")

        for root in actualNode.adjacencyList:
            if not root.visited:
                queue.append(root)


node1 = Node("1")
node2 = Node("2")
node3 = Node("3")
node4 = Node("4")
node5 = Node("5")

node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node2.adjacencyList.append(node5)

# node1.adjacencyList.append(node2)
# node1.adjacencyList.append(node3)
# node2.adjacencyList.append(node4)
# node4.adjacencyList.append(node5)

bfs_traverse(node1)