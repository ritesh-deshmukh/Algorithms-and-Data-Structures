# write a method to create a binary tree from a sorted input array. Try to limit the height of the tree.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def arr_bst(arr):
    if not arr:
        return None

    mid = len(arr)//2

    root = Node(arr[mid])

    root.left = arr_bst(arr[:mid])
    root.right = arr_bst(arr[mid+1:])

    return root

def preOrder(node):
    if not node:
        return
    print(node.data)
    preOrder(node.left)
    preOrder(node.right)


arr = [1, 2, 3, 4, 5, 6, 7]
root = arr_bst(arr)
preOrder(root)