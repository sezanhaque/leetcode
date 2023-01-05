from collections import deque
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = deque()
        res = []

        def backtrack(open: int, close: int):
            # if open == close == n then
            # we append the stack to res
            # and return
            if open == close == n:
                res.append("".join(stack))
                return

            # if open < n it means
            # we can add opening parenthesis
            if open < n:
                stack.append("(")
                backtrack(open + 1, close)
                # after backtracking we now
                # pop the open parenthesis
                stack.pop()

            if close < open:
                stack.append(")")
                backtrack(open, close + 1)
                # after backtracking we now
                # pop the close parenthesis
                stack.pop()

        backtrack(0, 0)
        return res


obj = Solution()
print(obj.generateParenthesis(3))
