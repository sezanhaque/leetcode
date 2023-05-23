import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k

        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)

        return self.heap[0]


nums, stream = [4, 5, 8, 2], [3, 5, 10, 9, 4]
obj = KthLargest(3, nums)
for i in range(0, len(stream)):
    print(obj.add(stream[i]), " ", end='')
