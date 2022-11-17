"""
    *** Premium
    Monotonic Stack - Strictly decreasing
    Que link: https://leetcode.ca/2021-04-14-1762-Buildings-With-an-Ocean-View/

    A building has ocean view if all buildings on its right are smaller than this building.

    Problem type    -   next greater
    Stack type      -   monotonic strictly decreasing
    Operator        -   <=
"""

from collections import deque


class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        stack = deque()

        for idx, val in enumerate(heights):
            while stack and heights[stack[-1]] <= val:
                stack.pop()
            stack.append(idx)

        return stack


print(Solution.findBuildings(0, heights=[4, 2, 3, 1]))  # [0,2,3]
