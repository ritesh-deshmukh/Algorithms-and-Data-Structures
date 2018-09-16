# Given a singly linked list, find middle of the linked list.
# For example, if given linked list is 1->2->3->4->5 then output should be 3.

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class linked(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.count += 1
            self.head = new_node
        else:
            self.count += 1
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def display(self):
        actualNode = self.head
        print(f"Count: {self.count}")
        # mid = self.count // 2
        temp_arr = []
        # print(f"Mid element: {mid}")
        while actualNode is not None:
            print(actualNode.data)
            temp_arr.append(actualNode.data)
            actualNode = actualNode.next
            # self.count -= 1
        # print(f"Middle element is {temp_arr[-1]}")
        print(temp_arr)
        print(temp_arr[len(temp_arr)//2])




ll = linked()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.insert(7)

ll.display()