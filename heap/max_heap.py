class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        value_index = len(self.storage) - 1
        self._bubble_up(value_index)

    def delete(self):
        max_value = self.storage[0]
        self.storage[0] = self.storage[len(self.storage) - 1]
        self.storage.pop()

        self._sift_down(0)
        return max_value

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
        max_index = len(self.storage) - 1
        left_child = (2 * index) + 1

        while left_child <= max_index:
            right_child = left_child + 1
            if right_child <= max_index and self.storage[right_child] > self.storage[left_child]:
                left_child = right_child

            if self.storage[left_child] > self.storage[index]:
                self.storage[left_child], self.storage[index] = self.storage[index], self.storage[left_child]
                index = left_child
                left_child = (2 * index) + 1

            else:
                break
