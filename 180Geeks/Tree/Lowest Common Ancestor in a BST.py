# Given a Binary Search Tree and 2 nodes value n1 and n2  ,
# your task is to find the lowest common ancestor of the two nodes


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def lowest_common_ancestor(root, n1, n2):
    if root is None:
        return

    if root.data > n1 and root.data > n2:
        return lowest_common_ancestor(root.left, n1, n2)

    if root.data < n1 and root.data < n2:
        return lowest_common_ancestor(root.right, n1, n2)

    return root


root = Node(5)
root.left = Node(4)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(3)
root.right.left = Node(7)
root.right.right = Node(8)


n1, n2 = 5, 8
lca_soln = lowest_common_ancestor(root, n1, n2)
print(f"LCA for {n1} and {n2}: {lca_soln.data}")