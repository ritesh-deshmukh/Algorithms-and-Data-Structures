# Depth first search for Graph

class Node(object):
    def __init__(self, data):
        self.data = data
        self.adjacencyList = []
        self.visited = False

def dfs_traverse(node):
    node.visited = True
    print(f"{node.data}", end=" ")

    for root in node.adjacencyList:
        if not root.visited:
            # root.visited = True
            dfs_traverse(root)



node1 = Node("1")
node2 = Node("2")
node3 = Node("3")
node4 = Node("4")
node5 = Node("5")

node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node2.adjacencyList.append(node5)

dfs_traverse(node1)
