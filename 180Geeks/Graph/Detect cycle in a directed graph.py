# Given a directed graph  your task is to complete the method isCycle  to detect if there is a cycle in the graph or not.

class Node:
    def __init__(self, name):
        self.name = name
        self.adjacencyList = []
        self.visited = False
        self.loop = False

class DepthFirstSearch:
    def dfs(self, node):
        node.visited = True
        # print(node.name, end=" ")

        for node in node.adjacencyList:
            if not node.visited:
                self.dfs(node)
            else:
                self.loop = True

        if self.loop == True:
            print("Found cycle")
        else:
            print("Not found cycle")


node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node0.adjacencyList.append(node2)
# node2.adjacencyList.append(node0)
node0.adjacencyList.append(node1)
node1.adjacencyList.append(node2)
node2.adjacencyList.append(node3)
# node3.adjacencyList.append(node3)

dfs = DepthFirstSearch()
dfs.dfs(node2)