from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1

        for num in nums:
            if not num:
                return 0
            
            product *= num

        return -1 if product < 0 else 1



obj = Solution()
print(obj.arraySign([-1,-2,-3,-4,3,2,1]))