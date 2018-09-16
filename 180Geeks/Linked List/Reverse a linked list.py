# Given pointer to the head node of a linked list, the task is to reverse the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked:
    def __init__(self):
        self.head = None

    def insert(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def display(self):
        actualNode = self.head
        while actualNode:
            print(actualNode.data, end=" ")
            actualNode = actualNode.next

    def reverseIterative(self):
        previous = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def reverseUtil(self, curr, prev):
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return
        next = curr.next
        curr.next = prev
        self.reverseUtil(next, curr)

    def reverse(self):
        if self.head is None:
            return
        self.reverseUtil(self.head, None)


ll = Linked()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
print("Traverse LL")
ll.display()
print("\nReversed LL using recursive approach")
ll.reverse()
ll.display()
print("\nReversed LL using iterative approach")
ll.reverseIterative()
ll.display()