class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LL(object):
    def __init__(self):
        self.head = None

    def insertBeginning(self, data):
        newNode = Node(data)

        if not self.head:
            newNode.prev = None
            self.head = newNode
            return
        # else:
        #     newNode.next = self.head
        #     self.head = newNode

        last = self.head
        while last.next is not None:
            last = last.next
        last.next = newNode
        newNode.prev = last
        return

    def traverseLL(self):
        actualNode = self.head
        while actualNode is not None:
            print(f"{actualNode.data}", end=" ")
            actualNode = actualNode.next

    def reverseLL(self):
        prev = None
        current = self.head

        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

ll = LL()

ll.insertBeginning(1)
ll.insertBeginning(2)
ll.insertBeginning(3)
ll.insertBeginning(4)
ll.insertBeginning(5)

ll.traverseLL()
ll.reverseLL()
print("\n")
ll.traverseLL()