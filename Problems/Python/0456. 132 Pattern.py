from itertools import accumulate
from math import inf


class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        """
        We consider the largest possible last_number so that the nums[i] < last_number 
        check has the largest possible range of values of nums[i] for it to return true. 
        (We can guarantee that last_number is the largest possible second number for the 
        current index since we popped it from stack, which is monotonically decreasing.) 
        Consider the following example:

        nums = [ 1, 4, 3, 2 ]

        When idx = 3, stack = [ ], last_number = -inf
        When idx = 2, stack = [2], last_number = -inf
        When idx = 1, stack = [3], last_number = 2
        When idx = 0, stack = [4], last_number = 3

        132 pattern found: ( 1, 4, 3 )
        """
        if len(nums) < 3:
            return False

        stack = []
        last_number = -inf

        for n in nums[::-1]:
            if n < last_number:
                # lowest number will be current number "n"
                # biggest number will be (middle one) in the stack
                # second big number will be last_number
                return True
            while stack and stack[-1] < n:
                last_number = stack.pop()
            stack.append(n)
        return False


# print(Solution.find132pattern(0, [1, 2, 3, 4]))  # false
print(Solution.find132pattern(0, [1, 4, 3, 2]))  # true
# print(Solution.find132pattern(0, [3, 1, 4, 2]))  # true
# print(Solution.find132pattern(0, [-1, 3, 2, 0]))  # true
print(Solution.find132pattern(0, [3, 5, 0, 3, 4]))  # true -> 3, 5, 4
