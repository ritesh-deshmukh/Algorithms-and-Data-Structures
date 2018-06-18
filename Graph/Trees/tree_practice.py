class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if data < node.data:
            if node.leftchild:
                self.insertNode(data, node.leftchild)
            else:
                node.leftchild = Node(data)
        else:
            if node.rightchild:
                self.insertNode(data, node.rightchild)
            else:
                node.rightchild = Node(data)

# Get minimum value
    def getMinValue (self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self, node):
        if node.leftchild:
            return self.getMin(node.leftchild)
        print(node.data)
        return node.data

# Get maximum value
    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)

    def getMax(self, node):
        if node.rightchild:
            return self.getMax(node.rightchild)
        print(node.data)
        return node.data

# Traversing through the tree
    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)
    # Traverse in order: left-root-right
    def traverseInOrder(self, node):
        if node.leftchild:
            self.traverseInOrder(node.leftchild)

        print("{}".format(node.data))

        if node.rightchild:
            self.traverseInOrder(node.rightchild)


bst = BinarySearchTree()
bst.insert(20)
bst.insert(10)
bst.insert(30)
bst.insert(45)
bst.insert(40)
bst.insert(23)
bst.insert(19)
bst.insert(60)
bst.insert(41)
print("Traversing through the tree InOrder:")
bst.traverse()
print("\n")
print("Get Minimum value:")
bst.getMinValue()
print("\n")
print("Get Maximum value:")
bst.getMaxValue()