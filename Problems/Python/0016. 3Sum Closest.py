from math import inf


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)

        nums.sort()
        minSum, minDiff = None, inf

        for idx in range(len(nums) - 2):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            left, right = idx + 1, len(nums) - 1

            while left < right:
                currSum = sum([nums[idx], nums[left], nums[right]])
                currDiff = abs(target - currSum)

                if currDiff < minDiff:
                    minDiff = currDiff
                    minSum = currSum
                    if minDiff == 0:
                        return minSum

                if target > currSum:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                else:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return minSum

    def threeSumClosest(self, nums: list[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)

        nums.sort()
        minDiff = inf

        for idx in range(len(nums) - 2):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            left, right = idx + 1, len(nums) - 1

            while left < right:
                currSum = sum([nums[idx], nums[left], nums[right]])

                if abs(target - minDiff) > abs(target - currSum):
                    minDiff = currSum

                if currSum == target:
                    return target
                elif currSum < target:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return minDiff


print(Solution.threeSumClosest(0, [-1, 2, 1, -4], 1))  # 2
print(Solution.threeSumClosest(0, [0, 0, 0], 1))  # 0
print(Solution.threeSumClosest(0, [1, 1, 1, 0], 100))  # 3
print(Solution.threeSumClosest(0, [1, 1, 1, 0], -100))  # 2
print(Solution.threeSumClosest(0, [4, 0, 5, -5, 3, 3, 0, -4, -5], -2))  # -2
print(Solution.threeSumClosest(0, [0, 3, 97, 102, 200], 300))  # 300
