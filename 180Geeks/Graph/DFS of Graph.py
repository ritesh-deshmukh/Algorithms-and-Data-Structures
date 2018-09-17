# Write a function to print the depth first traversal for a undirected graph from a given source s.

class Graph:
    def __init__(self):
        self.graph_dict = {}

    def addEdge(self, u, v):
        if not u in self.graph_dict.keys():
            self.graph_dict[u] = []
        self.graph_dict[u].append(v)

    def visited(self, v):
        visited_state = [False] * len(self.graph_dict)
        self.visitedUtil(v, visited_state)

    def visitedUtil(self, v, visited_state):
        visited_state[v] = True
        print(v, end=" ")

        for node in self.graph_dict[v]:
            if visited_state[node] == False:
                self.visitedUtil(node, visited_state)

dfs = Graph()
dfs.addEdge(0, 1)
dfs.addEdge(0, 2)
dfs.addEdge(1, 2)
dfs.addEdge(2, 0)
dfs.addEdge(2, 3)
dfs.addEdge(3, 3)

dfs.visited(0)