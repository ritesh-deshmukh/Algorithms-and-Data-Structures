class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)

        if not self.head:
            self.head = newNode

        else:
            newNode.next = self.head
            self.head = newNode

    def traverseLL(self):
        actualNode = self.head
        while actualNode is not None:
            print("{}".format(actualNode.data), end=" ")
            actualNode = actualNode.next

    def reverse(self):
        previous = None
        current = self.head
        while current != None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous



ll = Linked()

ll.insert(4)
ll.insert(3)
ll.insert(2)
ll.insert(1)
ll.insert(5)
# 5 1 2 3 4
ll.traverseLL()
print("\n")
ll.reverse()
ll.traverseLL()