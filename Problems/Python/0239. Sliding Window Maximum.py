from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        queue = deque()
        ans = []
        left = right = 0

        while right < len(nums):
            # pop smaller values from queue
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()

            queue.append(right)

            # remove left value from queue
            if left > queue[0]:
                queue.popleft()

            # check if window cover k
            if (right + 1) >= k:
                ans.append(nums[queue[0]])
                left += 1
            right += 1

        return ans


print(Solution.maxSlidingWindow(0, nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
print(
    Solution.maxSlidingWindow(0, nums=[1, -1, 3, 2, 4, 3, 2, 1], k=3)
)  # [3,3,4,4,4,3]
