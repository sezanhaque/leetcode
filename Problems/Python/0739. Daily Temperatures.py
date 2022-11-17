from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack, ans = deque(), [0] * len(temperatures)

        for idx, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                ans[stack.pop()] = idx - stack[-1]
            stack.append(idx)

        return ans


print(Solution.dailyTemperatures(0, [73, 74, 75, 71, 69, 72, 76, 73]))
print(Solution.dailyTemperatures(0, [30, 40, 50, 60]))
print(Solution.dailyTemperatures(0, [30, 60, 90]))
