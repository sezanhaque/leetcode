import heapq
from typing import List


class Solution:
    """
    Solution:
        1.  Create a list that contain every pile in negative.

        2.  Make the list as e heap, so the biggest pile which
            is now negative will be in the top of the heap as
            in the lowest number.

        3.  Loop through k times and get the top number from
            heap and divide it by to and replace it.

        4.  Return - sum of heap (as the piles were in negative).

    Complexity:
        Time:   O(k + nlogn)
                n for heap creation and logn for heap operation

        Space:  O(n), heap length
    """

    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-num for num in piles]
        heapq.heapify(heap)

        for _ in range(k):
            heapq.heapreplace(heap, heap[0] >> 1)

        return -sum(heap)


obj = Solution()
print(obj.minStoneSum(piles=[5, 4, 9], k=2))
