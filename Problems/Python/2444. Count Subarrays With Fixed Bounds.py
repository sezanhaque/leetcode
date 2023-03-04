from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        left_idx = right_idx = bad_idx = -1

        for idx, num in enumerate(nums):
            if not minK <= num <= maxK:
                bad_idx = idx
            if num == minK:
                left_idx = idx
            if num == maxK:
                right_idx = idx

            res += max(0, min(left_idx, right_idx) - bad_idx)

        return res


obj = Solution()
print(obj.countSubarrays(nums=[1, 3, 5, 2, 7, 5], minK=1, maxK=5))
