# Given a Binary Tree,  print the bottom view from left to right.
# A node x is there in output if x is the bottommost node at its horizontal distance from root.
# Horizontal distance of left child of a node x is equal to horizontal distance of x minus 1,
# and that of right child is horizontal distance of x plus 1.

class node:
    def __init__(self, data):
        self.data = data
        self.hd = -1
        self.left = None
        self.right = None

def bottom_view(root):
    if root is None:
        return

    q = []
    map = dict()

    q.append(root)

    while len(q) > 0:
        p = q[0]
        del q[0]

        hd = p.hd
        map[hd] = p.data

        if p.left is not None:
            p.left.hd = hd - 1
            q.append(p.left)

        if p.right is not None:
            p.right.hd = hd + 1
            q.append(p.right)

    print(f"Bottom view: {list(map.values())}")



head = node(1)
head.left = node(2)
head.right = node(3)
head.left.left = node(4)
head.left.right = node(5)
head.right.right = node(6)
head.left.left.right = node(7)
head.right.right.left = node(8)
head.left.left.right.left = node(9)
head.left.left.right.left.left = node(10)
head.right.right.left.right = node(11)
head.hd = 0
bottom_view(head)

