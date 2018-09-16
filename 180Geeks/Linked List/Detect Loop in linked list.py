# Given a linked list, check if the the linked list has a loop. Linked list can contain self loop.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next is not None:
                last = last.next
            last.next = new_node

    def displayLL(self):
        actualNode = self.head
        while actualNode is not None:
            print(actualNode.data, end=" ")
            actualNode = actualNode.next

    def detectLoopUsingSet(self):
        map_set = set()
        temp = self.head
        while temp:
            if temp in map_set:
                return True
            map_set.add(temp)
            temp = temp.next
        return False

    def detectLoopUsingPointers(self):
        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.head.next.next.next.next.next = ll.head
# print("Given linked list")
# ll.displayLL()

print(f"Detect look using set: {ll.detectLoopUsingSet()}\n")
print(f"Detect look using pointers: {ll.detectLoopUsingPointers()}")
