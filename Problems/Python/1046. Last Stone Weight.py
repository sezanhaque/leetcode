import bisect
import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while stones:
            s1 = stones.pop()
            if not stones:
                return s1

            s2 = stones.pop()
            if s1 > s2:
                bisect.insort_left(stones, s1 - s2)

        return 0

    def lastStoneWeight(self, stones: List[int]) -> int:
        for idx, stone in enumerate(stones):
            stones[idx] = - stone

        heapq.heapify(stones)

        while stones:
            s1 = -heapq.heappop(stones)
            if not stones:
                return s1

            s2 = -heapq.heappop(stones)
            if s1 > s2:
                heapq.heappush(stones, s2 - s1)

        return 0


obj = Solution()
print(obj.lastStoneWeight([2, 7, 4, 1, 8, 1]))  # 8, 7, 4, 2, 1, 1
