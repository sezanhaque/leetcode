from math import comb
from typing import List


class Solution:
    """
    We separate all the elements into two lists, depending on whether they are less than or more than the root. 
    Then we recurse on those left and right sublist. The combination is for the macro ordering between left and right, 
    and the recursive factors are for the internal ordering of left and right themselves. 
    """

    def numOfWays(self, nums: List[int]) -> int:
        def helper(nums: List[int]) -> int:
            if len(nums) <= 2:
                return 1

            left = [num for num in nums if num < nums[0]]
            right = [num for num in nums if num > nums[0]]

            return comb(len(left) + len(right), len(right)) * helper(left) * helper(right)

        # 1 minus from the result because we don't count the original ordering.
        return (helper(nums) - 1) % (10**9 + 7)


obj = Solution()
print(obj.numOfWays([3, 4, 5, 1, 2]))
