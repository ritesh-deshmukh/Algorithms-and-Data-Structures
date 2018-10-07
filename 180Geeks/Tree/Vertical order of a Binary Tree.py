
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def findMinMax(node, minimum, maximum, hd):
    if node is None:
        return

    if hd < minimum[0]:
        minimum[0] = hd
    elif hd > maximum[0]:
        maximum[0] = hd

    findMinMax(node.left, minimum, maximum, hd - 1)
    findMinMax(node.right, minimum, maximum, hd + 1)


def printVerticalLine(node, line_no, hd):
    if node is None:
        return
    if hd == line_no:
        print(node.data)

    printVerticalLine(node.left, line_no, hd - 1)
    printVerticalLine(node.right, line_no, hd + 1)


def verticalOrder(root):
    minimum = [0]
    maximum = [0]
    findMinMax(root, minimum, maximum, 0)

    for line_no in range(minimum[0], maximum[0] + 1):
        printVerticalLine(root, line_no, 0)
        print()


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)

print("Vertical order traversal is")

verticalOrder(root)