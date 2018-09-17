# Write a function to print the bredth first traversal for a graph from a given source s.

class Node:
    def __init__(self, name):
        self.name = name
        self.adjacencyList = []
        self.visited = False

class BreadthFirstSearch:
    def bfs(self, node):
        node_queue = []
        node_queue.append(node)
        node.visited = True

        while node_queue:
            actualNode = node_queue.pop(0)
            print(actualNode.name, end=" ")

            for neighbor in actualNode.adjacencyList:
                if not neighbor.visited:
                    node_queue.append(neighbor)


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")

node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node4.adjacencyList.append(node5)

bfs = BreadthFirstSearch()
bfs.bfs(node1)
