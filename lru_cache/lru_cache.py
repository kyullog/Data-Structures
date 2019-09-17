from doubly_linked_list import DoublyLinkedList


class LRUCache:

    """
Our LRUCache class keeps track of the max number of nodes it
can hold, the current number of nodes it is holding, a doubly-
linked list that holds the key-value entries in the correct
order, as well as a storage dict that provides fast access
to every node stored in the cache.

- max number of nodes it can hold
- current number holding

- Want to hold hey-value entries in order
- We want to find the least-recently used entry, and delete, if max is reached
    - DLL: remove from the tail
    - Array: pop()
    - Array: if added to back, remove from front: unshift()
- We want to add things to the front:
    - Array: add to front
    - DLL: add to head

- Alt.: add to back of an array, then sort(), then pop() from the back

We shall use the DLL!

- We want fast access to all nodes in the cache
- We want many lookups by identity (key / value)
    - Most efficient is dictionary

We need two constants, and two data structures
    """

    # def __init__(self, limit=10):
    #     self.max_number_of_nodes = limit
    #     self.current_nodes = 0
    #     self.cache = {}
    #     self.order = DoublyLinkedList()
    def __init__(self, limit=10):
        self.max_number_of_nodes = limit
        self.current_nodes = 0
        self.cache = {}
        self.order = DoublyLinkedList()

    """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the front of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            value = node.value[1]
            self.order.move_to_front(node)

            return value

    """
  Case 1 : Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. 

  Case 2 : If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. 
  
  Case 3 : Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  
  """

    def set(self, key, value):
        # Case 3
        if key in self.cache:
            # overwrite the value in our DLL, self.order
            # move to front, it's most recently used
            node = self.cache[key]
            self.order.move_to_front(node)
            node.value = (key, value)
        else:
            # Case 2
            if self.current_nodes == self.max_number_of_nodes:
                oldest_thing = self.order.tail
                old_key = oldest_thing.value[0]
                del self.cache[old_key]
                self.order.remove_from_tail()
                self.current_nodes -= 1
            # Case 1
            self.order.add_to_head((key, value))
            self.cache[key] = self.order.head
            self.current_nodes += 1
