class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        value_index = len(self.storage) - 1
        self._bubble_up(value_index)

    def delete(self):
        pass

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.storage[parent_index] < self.storage[index]:
                self.storage[parent_index], self.storage[index] = self.storage[index], self.storage[parent_index]
                index = parent_index
            else:
                break

    def _sift_down(self, index):
        pass
