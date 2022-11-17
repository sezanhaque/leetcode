from collections import deque


class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        """
        *   Monotonic Stack
        *   Decreasing - every element of the stack is smaller than or equal to the previous element. 
        *   Stack type : decreasing (strict)
        *   Operator in while loop : stackTop <= current
        """
        stack = deque()
        ans = [0] * len(heights)

        for idx, val in enumerate(heights):
            # when height of last stack person
            # is equal or greater than current person
            # add 1 to the last stack person
            while stack and heights[stack[-1]] <= val:
                ans[stack.pop()] += 1

            # increment the previous greater
            # it means if there is any one in the stack
            # then he will see current person
            # so add his count
            if stack:
                ans[stack[-1]] += 1
            stack.append(idx)
        return ans


print(Solution.canSeePersonsCount(0, [10, 6, 8, 5, 11, 9]))
print(Solution.canSeePersonsCount(0, [5, 1, 2, 3, 10]))
