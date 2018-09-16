# Given a linked list, write a function to reverse every k nodes (where k is an input to the function).
# If a linked list is given as 1->2->3->4->5->6->7->8->NULL and k = 3 then output will be 3->2->1->6->5->4->8->7->NULL.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked:
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

    def displayLL(self):
        actualNode = self.head
        while actualNode:
            print(actualNode.data, end=" ")
            actualNode = actualNode.next

    def rotateByN(self, head, n):
        current = head
        previous = None
        next = None
        count = 0
        while current is not None and count < n:
            next = current.next
            current.next = previous
            previous = current
            current = next
            count += 1
        if next is not None:
            head.next = self.rotateByN(next, n)
        return previous



ll = Linked()
ll.insertEnd(1)
ll.insertEnd(2)
ll.insertEnd(3)
ll.insertEnd(4)
ll.insertEnd(5)
ll.insertEnd(6)
ll.insertEnd(7)
ll.insertEnd(8)
ll.insertEnd(9)
print("Given Linked List")
ll.displayLL()
print("\nReversed Linked List")
ll.head = ll.rotateByN(ll.head, 3)
ll.displayLL()