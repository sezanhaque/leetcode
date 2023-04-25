import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.priority_queue = []

        for idx in range(1, 1001):
            heapq.heappush(self.priority_queue, idx)

    def popSmallest(self) -> int:
        if self.priority_queue:
            return heapq.heappop(self.priority_queue)
        return -1

    def addBack(self, num: int) -> None:
        if num not in self.priority_queue:
            heapq.heappush(self.priority_queue, num)


obj = SmallestInfiniteSet()
obj.addBack(2)
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())
obj.addBack(1)
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())
