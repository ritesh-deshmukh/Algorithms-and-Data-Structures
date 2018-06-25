class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        # self.size = 0

    def insertStart(self, data):
        # self.size += 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def insertEnd(self, data):
        # self.size += 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
        actualNode.nextNode = newNode

    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print("{}".format(actualNode.data))
            actualNode = actualNode.nextNode
    #
    # def size(self):
    #     return self.size

    def size2(self):
        actualNode = self.head
        size =0

        while actualNode is not None:
            size += 1
            actualNode = actualNode.nextNode
        return size


ll = LinkedList()
ll.insertStart(1)
ll.insertStart(2)
ll.insertStart(3)
ll.insertStart(4)
ll.insertEnd(5)
ll.insertEnd(6)
ll.insertEnd(7)
ll.insertEnd(8)

print(ll.size2())
# ll.traverseList()
