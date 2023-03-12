from collections import Counter
from typing import List


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        res = prefix = 0
        counter = Counter([0])

        for num in nums:
            prefix ^= num
            res += counter[prefix]
            counter[prefix] += 1

        return res


obj = Solution()
print(obj.beautifulSubarrays([4, 3, 1, 2, 4]))
