import bisect
from math import inf
from typing import List
from sortedcontainers import SortedSet


class SummaryRanges:
    # Using SortedSet

    def __init__(self):
        # we are using SortedSet so that we can add and retrieve
        # any value on O(logn) time, so intervals will be okay.
        self.nums = SortedSet()

    def addNum(self, value: int) -> None:
        self.nums.add(value)

    def getIntervals(self) -> List[List[int]]:
        intervals = []

        for num in self.nums:
            # if we have any interval then
            # check if the end of last interval + 1
            # equals to current num, it means there is
            # a continuous number, so add update the num
            if intervals and intervals[-1][1] + 1 == num:
                intervals[-1][1] = num
            else:
                intervals.append([num, num])

        return intervals


class SummaryRanges:
    # Using binary search time complexity O(logn)

    def __init__(self):
        self.intervals = [[-inf, -inf], [inf, inf]]

    def addNum(self, val: int) -> None:
        # using binary search we are searching the index
        # where we can insert the val
        idx = bisect.bisect(self.intervals, [val])

        prev_start, prev_end = self.intervals[idx - 1]
        next_start, next_end = self.intervals[idx]

        # [[1,2], [4,5]] + 3 -> merge two intervals into [[1,5]]
        if prev_end == val - 1 and next_start == val + 1:
            self.intervals = self.intervals[:idx - 1] + [[prev_start, next_end]] + self.intervals[idx + 1:]

        # [[1,2], [5,6]] + 3 -> update [1,2] to [1,3]
        elif prev_end == val - 1:
            self.intervals[idx - 1][1] = val

        # [[1,2], [5,6]] + 4 -> update [5,6] to [4,6]
        elif next_start == val + 1:
            self.intervals[idx][0] = val

        # [[1,2], [6,7]] + 4 -> add another interval [4,4]
        elif prev_end < val - 1 and next_start > val + 1:
            self.intervals = self.intervals[:idx] + [[val, val]] + self.intervals[idx:]

    def getIntervals(self) -> List[List[int]]:
        # we filter first and last index as they are inf
        return self.intervals[1:-1]


obj = SummaryRanges()
obj.addNum(1)
print(obj.getIntervals())
obj.addNum(3)
print(obj.getIntervals())
obj.addNum(7)
print(obj.getIntervals())
obj.addNum(2)
print(obj.getIntervals())
obj.addNum(6)
print(obj.getIntervals())
