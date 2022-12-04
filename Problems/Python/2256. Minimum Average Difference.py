from math import inf


class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        # fast
        length = len(nums)
        rightSum = sum(nums)
        leftSum = index = 0
        minAvg = inf

        for idx in range(length):
            leftSum += nums[idx]
            rightSum -= nums[idx]

            leftAvg = leftSum // (idx + 1)

            if idx == length - 1:
                rightAvg = 0
            else:
                rightAvg = rightSum // (length - idx - 1)

            avg = abs(leftAvg - rightAvg)

            if avg < minAvg:
                minAvg = avg
                index = idx

        return index

    def minimumAverageDifference(self, nums: list[int]) -> int:
        length = len(nums)
        prefix = index = 0
        suffix = sum(nums)
        minAvg = inf

        for idx in range(length):
            prefix += nums[idx]
            suffix -= nums[idx]

            avg = abs(
                (prefix // (idx + 1)) - (suffix // (length - idx - 1 or 1))
            )  # or used to get 1 if len - idx - 1 is 0

            if avg < minAvg:
                minAvg = avg
                index = idx

        return index


print(Solution.minimumAverageDifference(0, [4, 2, 0]))
print(Solution.minimumAverageDifference(0, [2, 5, 3, 9, 5, 3]))
print(Solution.minimumAverageDifference(0, [0]))
