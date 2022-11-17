from collections import deque
from math import inf


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        *   Monotonic Stack
        *   Strictly increasing - every element of the stack is strictly greater than the previous element.
        *   Stack type : increasing (strict)
        *   Operator in while loop : stackTop >= current
        """

        stack = deque()
        maxArea = 0
        # to calculate last index of heights
        # we need to add extra index so that we can
        # calculate from new index for original last index
        heights += [0]

        for idx, currVal in enumerate(heights):
            """
            We are checking while every value (idx) in the stack is greater than current value,
            then pop the bigger height from stack as height of the rectangle
            then calculate the distance between current index and the height of bigger bar
            this height * width will be the total area.
            """
            while stack and heights[stack[-1]] >= currVal:
                height = heights[stack.pop()]
                width = idx if not stack else idx - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(idx)
        return maxArea


# print(Solution.largestRectangleArea(0, [2, 1, 5, 6, 2, 3]))  # 10
# print(Solution.largestRectangleArea(0, [2, 0, 2]))  # 2
print(Solution.largestRectangleArea(0, [2, 4]))  # 4
# print(Solution.largestRectangleArea(0, [2, 1, 2]))  # 3
# print(Solution.largestRectangleArea(0, [2, 2, 2, 1, 1, 1, 1]))  # 7
