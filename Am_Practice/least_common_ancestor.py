# Given a binary tree (not a binary search tree) and two values say n1 and n2,
# write a program to find the least common ancestor

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def test(root, n1, n2):
    if root is None:
        return None

    if root.key == n1 or root.key == n2:
        return root

    left_lc = test(root.left, n1, n2)
    right_lc = test(root.right, n1, n2)

    if left_lc and right_lc:
        return root

    return left_lc if left_lc is not None else right_lc


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print("LCA(4,5) = ", test(root, 4, 5).key)
print("LCA(4,6) = ", test(root, 4, 6).key)
print("LCA(3,4) = ", test(root, 3, 4).key)
print("LCA(2,4) = ", test(root, 2, 4).key)