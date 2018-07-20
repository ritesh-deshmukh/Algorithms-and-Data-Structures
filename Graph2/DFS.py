# DFS is implemented using recursion
# But the operating system uses stack to store and process data
# Time complexity => O(logn) preferred than BFS - Memory friendly
# Node after node in DFS

class Node(object):
    def __init__(self, name):
        self.name = name
        self.adjacencyList = []
        self.visited = False
        # print(self.adjacencyList)

class DepthFirstSearch(object):
    def dfs(self, node):
        node.visited = True
        print("{}".format(node.name))

        for n in node.adjacencyList:
            if not n.visited:
                self.dfs(n)


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")

node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node4.adjacencyList.append(node5)
node1.adjacencyList.append(node5)

dfs = DepthFirstSearch()
dfs.dfs(node1)