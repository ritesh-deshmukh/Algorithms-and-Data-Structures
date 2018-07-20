class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Linked(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        # add to the start of the list
        newNode = Node(data)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode

    ###########################
    # add to the end of the list
    # newNode.next = None
    #
    # if not self.head:
    #     newNode.prev = None
    #     self.head = newNode
    #     return
    #
    # last = self.head
    # while last.next is not None:
    #     last = last.next
    # last.next = newNode
    # newNode.prev = last
    # return
    ############################
    # add to the end for singly linked list
    # else:
    #     newNode.next = self.head
    #     self.head = newNode

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
