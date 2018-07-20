class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.insertNode(data, node.leftChild)
            else:
                node.leftChild = Node(data)

        else:
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)

    def traverse(self):
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        if self.root:
            if node.leftChild:
                self.traverseInOrder(node.leftChild)
            print("{}".format(node.data), end=" ")
            if node.rightChild:
                self.traverseInOrder(node.rightChild)


bst = Tree()

bst.insert(20)
bst.insert(10)
bst.insert(30)
bst.insert(45)
bst.insert(40)
bst.insert(23)
bst.insert(19)
bst.insert(60)
bst.insert(41)

print("Traverse In Order ... ")
bst.traverse()