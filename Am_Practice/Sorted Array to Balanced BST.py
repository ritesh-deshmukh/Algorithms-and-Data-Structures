# Given a sorted array. Write a function that creates a Balanced Binary Search Tree using array elements.

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sort2BST(arr):
    if not arr:
        return None

    mid = len(arr)//2
    root = Node(arr[mid])
    root.left = sort2BST(arr[:mid])
    root.right = sort2BST(arr[mid+1:])
    return root

def preorder(node):
    if not node:
        return
    print(node.value, end=" ")
    preorder(node.left)
    preorder(node.right)


arr = [1,2,3,4,5,6]
root = sort2BST(arr)

print(f"Preorder Traversal")
preorder(root)