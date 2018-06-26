# In preorder, the root(parent) comes before the children. After parent comes left then right
# In postorder, the children(left then right) come before the root(parent).
# In inorder, the left tree comes then the root and then the right tree


class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.value == data:
            print("Value already in Tree")
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()
            print(str(self.value))

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.preorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.preorder()


class Tree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print("PreOrder")
        self.root.preorder()

    def postorder(self):
        print("PostOrder")
        self.root.postorder()

    def inorder(self):
        print("InOrder")
        self.root.inorder()


bst = Tree()
print(bst.insert(10))
print(bst.insert(15))
print(bst.insert(20))
# print(bst.insert(15))
bst.preorder()
bst.postorder()
bst.inorder()