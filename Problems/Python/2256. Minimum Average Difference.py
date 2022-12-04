from math import inf

class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        totalSum = sum(nums)
        length = len(nums)
        leftSum = leftIndexSum = 0
        rightSum = minIndex = 0
        minAvg = inf

        for idx, val in enumerate(nums):
            leftSum += val
            leftIndexSum += 1

            rightSum = totalSum - leftSum
            rightIndexSum = length - leftIndexSum

            if rightSum != 0 and rightIndexSum != 0:
                avg = abs((leftSum // leftIndexSum) - (rightSum // rightIndexSum))
                if avg < minAvg:
                    minAvg = avg
                    minIndex = idx
            else:
                avg = abs((leftSum // leftIndexSum))
                if avg < minAvg:
                    minAvg = avg
                    minIndex = idx
        
        return minIndex




print(Solution.minimumAverageDifference(0, [4, 2, 0]))
print(Solution.minimumAverageDifference(0, [2,5,3,9,5,3]))
print(Solution.minimumAverageDifference(0, [0]))