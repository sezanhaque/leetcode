class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        # Time Limit exceeded
        res, length = 0, len(nums)

        for idx in range(length):
            left, right = nums[idx], nums[idx]

            for j in range(idx, length):
                left, right = min(left, nums[j]), max(right, nums[j])
                res += right - left

        return res

    def subArrayRanges(self, nums: list[int]) -> int:
        # Link: https://leetcode.com/problems/sum-of-subarray-ranges/solutions/2722786/sum-of-subarray-ranges/
        
        n, answer = len(nums), 0
        stack = []

        # Find the sum of all the minimum.
        for right in range(n + 1):
            while stack and (right == n or nums[stack[-1]] >= nums[right]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                answer -= nums[mid] * (mid - left) * (right - mid)
            stack.append(right)

        # Find the sum of all the maximum.
        stack.clear()
        for right in range(n + 1):
            while stack and (right == n or nums[stack[-1]] <= nums[right]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                answer += nums[mid] * (mid - left) * (right - mid)
            stack.append(right)

        return answer


print(Solution.subArrayRanges(0, [1, 2, 3]))
