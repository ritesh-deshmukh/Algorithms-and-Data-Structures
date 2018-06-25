class DirectedGraph:
    linkCount = 0

    class Node:
        def __init__(self, data):
            self.data = data
            self.links = []

        def pointsTo(self, node):
            self.links.append(node)
            DirectedGraph.linkCount += 1

    def __init__(self):
        self.nodes = []
        self.nodeCount = 0

    def newNode(self, data):
        node = self.Node(data)
        self.nodes.append(node)
        self.nodeCount += 1
        return node

    def __repr__(self):
        result = ""
        for node in self.nodes:
            for link in node.links:
                result += "{} --> {}\n".format(node.data, link.data)
        print(result)
        return result


dg = DirectedGraph()
n0 = dg.newNode("A")
n1 = dg.newNode("B")
n2 = dg.newNode("C")
n0.pointsTo( n1 )
n1.pointsTo( n2 )
n2.pointsTo( n0 )
n2.pointsTo( n2 )
# assert dg.linkCount == 4
# assert dg.nodeCount == 3