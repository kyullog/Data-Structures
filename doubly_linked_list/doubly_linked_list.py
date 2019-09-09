"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
  as the new head of the list. Don't forget to handle
  the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """Removes the List's current head node, making the
  current head's next node the new head of the List.
  Returns the value of the removed Node."""

    def remove_from_head(self):
        return_value = self.head.value
        self.delete(self.head)
        return return_value

        # if self.head is None:
        #     return_value = None
        # elif self.head is self.tail:
        #     return_value = self.head
        #     self.head = None
        #     self.tail = None
        #     self.length = 0
        #     return return_value
        # else:
        #     self.head = self.head.next
        #     self.head.prev = None
        # self.length -= 1
        # return return_value

    """Wraps the given value in a ListNode and inserts it
  as the new tail of the list. Don't forget to handle
  the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_tail = ListNode(value)
        if not self.head and not self.tail:
            self.head = new_tail
            self.tail = new_tail
        else:
            new_tail.prev = self.tail
            self.tail.next = new_tail
            self.tail = new_tail

            new_tail.next = None
        self.length += 1


    """Removes the List's current tail node, making the
  current tail's previous node the new tail of the List.
  Returns the value of the removed Node."""

    def remove_from_tail(self):
        return_value = self.tail.value
        self.delete(self.tail)
        return return_value
        # if not self.tail:
        #     return_value = None
        # elif self.tail is self.head:
        #     return_value = self.tail.value
        #     self.tail = None
        #     self.head = None
        # else:
        #     return_value = self.tail.value
        #     self.tail = self.tail.prev
        #     self.tail.next = None
        # return return_value

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node is self.head:
            return
        elif node is self.tail:
            self.remove_from_tail()
        else:
            self.delete(node)
        self.add_to_head(node.value)

        # new_head = node
        # if self.head == new_head:
        #     return
        # if self.tail == new_head:
        #     prev_node = self.tail.prev
        #     prev_node.next = None
        #     self.tail = prev_node

        #     new_head.prev = None
        #     new_head.next = self.head
        #     self.head.prev = node
        #     self.head = node
        # else:
        #     prev_node = new_head.prev
        #     next_node = new_head.next
        #     old_head = self.head

        #     prev_node.next, next_node.prev = next_node, prev_node
        #     old_head.prev = new_head
        #     new_head.prev, new_head.next = None, old_head
        #     self.head = new_head

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node is self.tail:
            return
        elif node is self.head:
            self.remove_from_head()
        else:
            self.delete(node)

        self.add_to_tail(node.value)

        """Removes a node from the list and handles cases where
  the node was the head or the tail"""

    def delete(self, node):
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = self.head.next
            node.delete()
        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()
        else:
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        if self.head is None:
            return None
        max_val = self.head.value
        current = self.head
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val
