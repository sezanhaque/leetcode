from collections import defaultdict
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = reminder = 0
        reminderFreq = defaultdict(int)
        # empty list will have sum of 0 and reminder is also 0
        # therefore we are storing the occurrence of 0 as 1
        reminderFreq[0] = 1

        for num in nums:
            reminder = (reminder + num) % k
            res += reminderFreq[reminder]
            reminderFreq[reminder] += 1

        return res


obj = Solution()
print(obj.subarraysDivByK(nums=[4, 5, 0, -2, -3, 1], k=5))
