from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMin = currMax = totalSum = 0
        minSum = maxSum = nums[0]

        for num in nums:
            # kadane's algorithm to find min subarray sum
            currMax = max(num, currMax + num)
            maxSum = max(maxSum, currMax)

            # kadane's algorithm to find min subarray sum
            currMin = min(num, currMin + num)
            minSum = min(minSum, currMin)

            # compute the sum of list
            totalSum += num

        # if min sum is equal to total sum
        # then it means we have all negative value
        # then we have max value in max sum, return maxSum
        # or return max(maxSum, totalSum - minSum)
        # if minSum == totalSum:
        #     return maxSum
        # return max(maxSum, totalSum - minSum)

        # alternately we can say if maxSum < 0 then it means
        # we have all negative value in the array so return maxSum
        # otherwise return max(maxSum, totalSum - minSum)

        return max(maxSum, totalSum - minSum) if maxSum > 0 else maxSum


obj = Solution()
print(obj.maxSubarraySumCircular([1, -2, 3, -2]))  # 3
print(obj.maxSubarraySumCircular([5, -3, 5]))  # 10
print(obj.maxSubarraySumCircular([-3, -2, -3]))  # -2
print(obj.maxSubarraySumCircular([6, 9, -3]))  # 15
print(obj.maxSubarraySumCircular([2, -2, 2, 7, 8, 0]))  # 19
