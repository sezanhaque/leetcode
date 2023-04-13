from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        idx = 0
        stack = []

        for num in pushed:
            stack.append(num)

            while idx < len(popped) and stack and popped[idx] == stack[-1]:
                stack.pop()
                idx += 1

        return not stack


obj = Solution()
print(obj.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]))
