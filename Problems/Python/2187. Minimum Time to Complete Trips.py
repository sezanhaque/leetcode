from bisect import bisect_left
from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        start, end = 1, totalTrips * min(time)

        while start < end:
            need = (start + end) >> 1

            if sum(need // t for t in time) < totalTrips:
                start = need + 1
            else:
                end = need

        return start

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        return bisect_left(range(1, totalTrips * min(time)), totalTrips, key=lambda trip: sum(trip // t for t in time)) + 1


obj = Solution()
print(obj.minimumTime(time=[1, 2, 3], totalTrips=5))
