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
        self.limit = limit
        self.size = 0
        self.dll = DoublyLinkedList()
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            # move to the front
            self.dll.move_to_front(node)
            return node.value[1]
        else:
            return None

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
        # check to see if the value is already in the dictionary
        if key in self.storage:

            # update it with the new value
            node = self.storage[key]

            # move it to the front of the dll
            self.dll.move_to_front(node)
            node.value = (key, value)

            return

        # check to see if the cache is full - if length is at limit
        if self.size == self.limit:
            # if so, delete oldest item from both dll and storage
            self.storage.pop(self.dll.tail.value[0])
            self.dll.remove_from_tail()
            self.size -= 1

        # add key & value to the front of the dll as a tuple
        self.dll.add_to_head((key, value))

        # add key and node to the dictionary
        # the value of the key is the memory address of the node
        self.storage[key] = self.dll.head
        self.size += 1
        return
