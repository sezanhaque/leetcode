import heapq
from typing import List


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        half, operation = sum(nums) / 2, 0

        # create a list for heap
        heap = [-num for num in nums]

        # create a heap from the list
        heapq.heapify(heap)

        while half > 0:
            # pop the biggest number from heap
            num = -heapq.heappop(heap)

            # divide the number by 2
            num /= 2

            # reduce the half by num
            half -= num

            # push the num to heap
            heapq.heappush(heap, -num)

            operation += 1

        return operation


obj = Solution()
print(obj.halveArray([5, 19, 8, 1]))
