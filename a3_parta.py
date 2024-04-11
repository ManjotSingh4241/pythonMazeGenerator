class MinHeap:
    def __init__(self, arr=None):
       self.heap = [] if arr is None else arr[:]
       if arr is not None:
           for i in range(len(self.heap) // 2 - 1, -1, -1):
               self._heap_down(i)
         
    def _heapify(self):
        for i in reversed(range(len(self.heap) // 2)):
            self._heap_down(i)

    def insert(self, element):
        self.heap.append(element)
        self._heap_up(len(self.heap) - 1)

    def get_min(self):
        return self.heap[0] if self.heap else None

    def extract_min(self):
        if self.is_empty():
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min_element = self.heap.pop()
        self._heap_down(0)
        return min_element

    def is_empty(self):
        return len(self.heap) == 0

    def __len__(self):
        return len(self.heap)
    
    def _heap_up(self, sift):
        old_node = (sift - 1) / 2
        int_node = int(old_node)
        while True:
            while True:
                if self.heap[sift] >= self.heap[int_node]:
                    break
                elif sift <= 0:
                    break
                temp = self.heap[sift]
                self.heap[sift] = self.heap[int_node]
                self.heap[int_node] = temp
                sift = int_node
                int_node = (sift - 1) // 2
            break

    def _heap_down(self, i):
        left_child_i = 2 * i + 1
        right_child_i= 2 * i + 2
        smallest = i

        if left_child_i < len(self.heap) and self.heap[left_child_i] < self.heap[smallest]:
            smallest = left_child_i
        if right_child_i < len(self.heap) and self.heap[right_child_i] < self.heap[smallest]:
            smallest = right_child_i

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heap_down(smallest)
