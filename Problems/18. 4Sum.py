class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        length = len(nums) - 1
        nums.sort()
        ans = []

        for i in range(length - 2):
            if i >= 1 and nums[i] == nums[i - 1]:
                # this step makes sure that we do not have any duplicates in our result output
                continue

            for j in range(i + 1, length - 1):
                if j >= i + 2 and nums[j] == nums[j - 1]:
                    # this step makes sure that we do not have any duplicates in our result output
                    continue

                left, right = j + 1, length

                while left < right:
                    currList = [nums[i], nums[j], nums[left], nums[right]]
                    currSum = sum(currList)

                    if currSum == target:
                        ans.append(currList)
                        while left < right and nums[left + 1] == nums[left]:
                            # Another conditional for not calculating duplicates
                            left += 1
                        left += 1
                    elif currSum < target:
                        left += 1
                    elif currSum > target:
                        right -= 1
        return ans


# print(Solution.fourSum(0, [1, 0, -1, 0, -2, 2], 0))
# print(Solution.fourSum(0, [2, 2, 2, 2, 2], 8))
# print(Solution.fourSum(0, [0, 0, 0, 0], 0))
# print(Solution.fourSum(0, [0, 0, 0, 0], 1))
print(
    Solution.fourSum(0, [-2, -1, -1, 1, 1, 2, 2], 0)
)  # [[-2,-1, 1, 2], [-1,-1, 1, 1]]
print(Solution.fourSum(0, [-3, -2, -1, 0, 0, 1, 2, 3], 0))
