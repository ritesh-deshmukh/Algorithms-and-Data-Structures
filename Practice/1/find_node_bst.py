class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if data < node.data:
            if node.left:
                self.insertNode(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self.insertNode(data, node.right)
            else:
                node.right = Node(data)

    def traverse(self):
        if self.root:
            self.traverseOrder(self.root)

    def traverseOrder(self, node):
        current = self.root
        s = []
        done = 0
        while not done:
            if current is not None:
                s.append(current)
                current = current.left

            else:
                if len(s) > 0:
                    current = s.pop()
                    print(current.data, end=" ")
                    current = current.right

                else:
                    done = 1

    def traverse_recursive(self):
        if self.root:
            self.traverseOrder_recursive(self.root)

    def traverseOrder_recursive(self, node):
        if node.left:
            self.traverseOrder(node.left)

        print("{}".format(node.data), end=" ")

        if node.right:
            self.traverseOrder(node.right)

    def find(self, value):
        if self.root != Node:
            return self._find(value, self.root)
        else:
            return False

    def _find(self, value, node):
        if value == node.data:
            return node
        elif value < node.data and node.left != None:
            return self._find(value, node.left)
        elif value > node.data and node.right != None:
            return self._find(value, node.right)
        else:
            return False


bst = BST()
bst.insert(20)
bst.insert(10)
bst.insert(30)
bst.insert(45)
bst.insert(40)
bst.insert(23)
bst.insert(19)
bst.insert(60)
bst.insert(41)
bst.traverse()
print("\n")
bst.traverse_recursive()

# x = bst.find(1028)
# if not x:
#     print("Nai mila")
# else:
#     print(x.data)
# print(bst.find(1028).data)
# print(dir(bst.find))
