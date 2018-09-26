# Given a linked list, the task is to find the n'th node from the end.
# It is needed to complete a method that takes two argument, head of linked list and an integer n.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def insertEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.count += 1
        else:
            self.count += 1
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def display(self, n):
        actualNode = self.head
        print(f"Count = {self.count}")
        print_node = self.count - n
        # print(f"Nth node number: {print_node}")
        i = 0
        while actualNode and i != print_node:
            actualNode = actualNode.next
            i += 1
        print(f"Nth node: {actualNode.data}")


ll = LinkedList()
ll.insertEnd(10)
ll.insertEnd(20)
ll.insertEnd(30)
ll.insertEnd(40)
ll.insertEnd(50)
ll.insertEnd(60)
print("Original LL")
ll.display(2)