# An XOR linked list is a more memory efficient doubly linked list.
# Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node.
# Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
#
# If using a language that has no pointers (such as Python),
# you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

#
# class Node(object):
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.previous = None
#         self.xor = None
#
# class DLL(object):
#     def __init__(self):
#         self.head = None
#
#     def insert(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#
#         self.head = new_node
#
#     def traverse(self):
#         temp = self.head
#         while temp:
#             print(temp.data)
#             temp = temp.next
#
# dll = DLL()
# dll.insert(1)
# dll.insert(2)
# dll.insert(3)
# dll.insert(4)
#
# dll.traverse()
