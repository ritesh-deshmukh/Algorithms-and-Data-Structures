# Given a singly linked list, rotate the linked list counter-clockwise by k nodes.
# Where k is a given positive integer smaller than or equal to length of the linked list.
# For example, if the given linked list is 10->20->30->40->50->60 and k is 4, the list should be modified to 50->60->10->20->30->40.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def insertStart(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def display(self):
        actualNode = self.head
        while actualNode:
            print(actualNode.data, end=" ")
            actualNode = actualNode.next

    def reverseRecursive(self):
        if self.head is None:
            return
        self.reverseRecursiveUtil(self.head, None)

    def reverseRecursiveUtil(self, curr, prev):
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return
        next = curr.next
        curr.next = prev
        self.reverseRecursiveUtil(next, curr)

    def reverseIterative(self):
        previous = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def rotateByN(self, n):
        if n == 0:
            return
        current = self.head
        count = 1
        while count < n and current is not None:
            current = current.next
            count += 1
        if current is None:
            return
        nNode = current
        while current.next is not None:
            current = current.next
        current.next = self.head
        self.head = nNode.next
        nNode.next = None


ll = LinkedList()
ll.insertEnd(10)
ll.insertEnd(20)
ll.insertEnd(30)
ll.insertEnd(40)
ll.insertEnd(50)
ll.insertEnd(60)
print("Original LL")
ll.display()
# ll.reverseRecursive()
# print("\nReversed LL recursively")
# ll.reverseRecursive()
# ll.display()
# print("\nReversed LL iteratively")
# ll.reverseIterative()
# ll.display()
print("Rotating by n = 4")
ll.rotateByN(4)
ll.display()