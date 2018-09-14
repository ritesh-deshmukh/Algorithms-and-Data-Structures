class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def appendtostart(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node
        new_node.prev = self.head

    def appendtoend(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def appendinmiddle(self, prev_node, new_data):
        if not prev_node:
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

    def printLL(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

llist = LinkedList()

llist.appendtostart(5)
llist.appendtostart(4)
llist.appendtostart(3)
llist.appendtostart(2)
llist.appendtostart(1)
llist.appendtoend(6)
llist.appendtoend(7)
llist.appendtoend(8)
llist.appendinmiddle(llist.head.next, 41)

llist.printLL()