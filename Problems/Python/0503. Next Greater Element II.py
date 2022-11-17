from collections import deque


class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack, ans = deque(), [-1] * len(nums)

        for idx, val in enumerate(nums):
            while stack and nums[stack[-1]] < val:
                ans[stack.pop()] = val
            stack.append(idx)

        for val in nums:
            while stack and nums[stack[-1]] < val:
                ans[stack.pop()] = val
            if not stack:
                break

        return ans

    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack, ans = deque(), [-1] * len(nums)

        for idx in list(range(len(nums))) * 2:

            # Check if stack and
            # right most value from stack which indicate idx
            # which index in nums is less than current index
            while stack and nums[stack[-1]] < nums[idx]:

                # If so then use right most value from stack
                # as index and assign current value to that index
                ans[stack.pop()] = nums[idx]

            # Store the index of the value
            # as it is the same list
            stack.append(idx)

        return ans


print(Solution.nextGreaterElements(0, nums=[1, 2, 3, 4, 3]))  # [2,3,4,-1,4]
print(Solution.nextGreaterElements(0, nums=[5, 4, 3, 2, 1]))  # [-1,5,5,5,5]
