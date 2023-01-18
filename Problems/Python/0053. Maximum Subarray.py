from typing import List


class Solution:
    """
    Kadane's algorithm
    """
    def maxSubArray(self, nums: List[int]) -> int:
        currSum, maxSum = 0, nums[0]

        for num in nums:
            # if current sum is less than 0
            # then we should make it 0
            # otherwise it will go to negative value
            if currSum < 0:
                currSum = 0
            currSum += num

            maxSum = max(maxSum, currSum)

        return maxSum


obj = Solution()
print(obj.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
