import heapq
from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        min_heap, max_heap = [], 0

        for num in nums:
            tmp = num

            # while the num is even
            # divide it by 2
            while not num & 1:
                num >>= 1

            min_heap.append((num, max(tmp, num << 1)))
            max_heap = max(max_heap, num)

        res = float('inf')
        heapq.heapify(min_heap)

        while len(min_heap) == len(nums):
            num, num_max = heapq.heappop(min_heap)
            res = min(res, max_heap - num)

            if num < num_max:
                num <<= 1
                heapq.heappush(min_heap, (num, num_max))
                max_heap = max(max_heap, num)

        return res

    def minimumDeviation(self, nums: List[int]) -> int:
        """
        Since numbers only become smaller, we can start with the largest number
        1 compare it with min number
        2 Divide it by 2 and put it back
        """

        heap = list(set(-(num << 1 if num & 1 else num) for num in nums))
        heapq.heapify(heap)

        max_heap, min_heap = -heap[0], -max(heap)
        res = max_heap - min_heap

        # while top heap is even
        while not heap[0] & 1:
            # Divide max by 2, num can not change any more because * once and / once
            num = heapq.heappop(heap) >> 1
            heapq.heappush(heap, num)
            max_heap, min_heap = -heap[0], min(min_heap, -num)
            res = min(res, max_heap - min_heap)

        return res


obj = Solution()
print(obj.minimumDeviation([1, 2, 3, 4]))
