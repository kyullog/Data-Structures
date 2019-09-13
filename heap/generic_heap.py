# When we add something to a heap, we add it as far
# to the left as we can

'''
Math for indexing our heap/tree


find parent: child_index // 2
'''


class Heap:
    def __init__(self, comparator):
        self.storage = []  # stored in very specific order
        self.comparator = comparator

    def insert(self, value):
        self.storage.append(value)
        value_index = len(self.storage) - 1
        self._bubble_up(value_index)

    def delete(self):
        """
        store what's at the front
        put the smallest value at the front, then remove it from
        our storage
        call sift down
        return value
        """
    pass

    def get_priority(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        '''
        While index > 0
        get teh parent
        if child is greater than parent --> comparator(child, parent)
        swap them

        if not, then we're still inside the while loop, but we have
        nothing to do,
        so break
        '''
    pass

    def _sift_down(self, index):
        '''
        while index is less than max index
        look at both children, choose the biggest
        left child: 2 * index, + 1
        right child: 2 * index, + 2
        swap with that child, if the chosen one is larger, update the index to the new location
        otherwise break out of your loop
        '''
    pass
