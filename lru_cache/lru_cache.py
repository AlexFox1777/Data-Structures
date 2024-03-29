import sys

sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.capacity = 0
        self.limit = limit
        self.hash_table = {}
        self.storage = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        self.storage.move_to_front(key)
        return self.hash_table.get(key)

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        if self.hash_table.get(key) is not None:
            # overwrite item in the hash table
            self.hash_table[key] = value
            return

        # add a new item in the list
        if self.capacity < self.limit:
            self.capacity += 1
            # write item at the beginning of the list
            self.storage.add_to_head(key)
        else:
            self.storage.add_to_head(key)
            self.storage.remove_from_tail()
            del self.hash_table[self.storage.tail.value]

        # write item in the hash table
        self.hash_table[key] = value


class LRUCache:

    def __init__(self, limit=10):
        self.size = 0
        self.limit = limit
        self.storage = {}
        self.order = DoublyLinkedList()

    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_end(node)
            return node.value[1]
        else:
            return None

    def set(self, key, value):
        # Check and see if key in cash
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_end(node)
            return

        # If it is in the cash move to front and update value
        if self.size == self.limit:
            del self.storage[self.order.head.value[0]]
            self.order.remove_from_tail()
            self.size -= 1

        # If not add to front of the cash
        # Deleting tail as most recent and head as most oldest
        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail
        self.size += 1
