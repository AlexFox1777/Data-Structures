class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

    def __repr__(self):
        return f"{self.value}"

class SingleLinkedList:
    def __init__(self, node = None):
        self.head = node
        self.length = 0

    def get_list(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    # insert a new node at the beginning
    def add_node(self, val):
        self.length += 1
        if self.head is None:
            self.head = val
        else:
            val.next = self.head
            self.head = val

    def reverse_list(self):
        current_node = self.head
        prev = None
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_node
        self.head = prev


list = SingleLinkedList()
list.add_node(Node(1))
list.add_node(Node(2))
list.add_node(Node(3))
list.add_node(Node(4))
list.add_node(Node(5))
list.get_list()
print('======reverse========')
list.reverse_list()
list.get_list()


