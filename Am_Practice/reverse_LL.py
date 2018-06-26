class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class rev_ll:
    def __init__(self):
        self.head = None

    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


ll = rev_ll()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)

print("Given Linked List =")
ll.printlist()

ll.reverse()
print("reversed Linked List = ")
ll.printlist()