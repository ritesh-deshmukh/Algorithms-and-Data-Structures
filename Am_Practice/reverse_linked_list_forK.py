# Python program to reverse a linked list in group of given size

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def reverse(self, head, k):

        current = head
        count = 0
        next = None
        prev = None

        while current is not None and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        if next is not None:
            head.next = self.reverse(next, k)
        return prev

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printLL(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


llist = LL()

llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print("The linked list is = ")
llist.printLL()

llist.head = llist.reverse(llist.head, 3)

print("The reversed String is = ")
llist.printLL()