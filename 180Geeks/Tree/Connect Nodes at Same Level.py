# Write a function to connect all the adjacent nodes at the same level in a binary tree.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.data, repr(self.next))


class Solution:
    def connect(self, root):
        head = root
        while head:
            cur, next_head = head, None
            while cur and cur.left:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            head = head.left


if __name__ == "__main__":
    root, root.left, root.right = Node(1), Node(2), Node(3)
    root.left.left, root.left.right, root.right.left, root.right.right = Node(4), Node(5), Node(6), Node(7)
    Solution().connect(root)
    print(root)
    print(root.left)
    print(root.left.left)