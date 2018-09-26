# Given a Linked List where every node represents a linked list and contains two pointers of its type:
# (i) a next pointer to the next node
# (ii) a bottom pointer to a linked list where this node is head.
# You have to flatten the linked list to a single linked list which is sorted.

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        self.child = None

    def __repr__(self):
        return str(self.value)

one = Node(1)
two = Node(2)
three = Node(3)
five = Node(5)
six = Node(6)
seven = Node(7)
eight = Node(8)
nine = Node(9)
one.next = two
two.prev = one
two.next = three
two.child = six
three.prev = two
three.next = five
five.prev = three
five.child = eight
six.next = seven
seven.prev = six
seven.child = nine

def flatten(head):
    if not head: return head

    c = flatten(head.child)
    n = flatten(head.next)
    if c:
        head.next = head.child
        head.child.prev = head
    if c and n:
        tail = c
        while tail.next:
            tail = tail.next
        tail.next = n
        n.prev = tail
    return head

n = flatten(one)
while n:
    print(f"{n.value} ", end=" ")
    n = n.next