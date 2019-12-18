import sys

sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


# class Queue:
#     def __init__(self):
#         self.size = 0
#         # Why is our DLL a good choice to store our elements?
#         self.storage = []
#
#     # adds an element to the end of the queue
#     def enqueue(self, value):
#         self.storage.insert(0, value)
#         self.size += 1
#
#     # removes the element at the beginning of the queue
#     def dequeue(self):
#         self.storage = self.storage[:-1]
#         self.size -= 1
#
#     def len(self):
#         return self.size

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    # adds an element to the end of the queue
    def enqueue(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    # removes the element at the beginning of the queue
    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_tail()
        else:
            return None


    def len(self):
        return self.size

