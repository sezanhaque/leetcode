class Solution:
    def numberOfSteps(self, num: int) -> int:
        return Solution.helper(self, num)

    def helper(self, num: int, steps: int = 0) -> int:
        if num == 0:
            return steps

        if not num & 1:
            return Solution.helper(self, num >> 1, steps + 1)
        else:
            return Solution.helper(self, num - 1, steps + 1)


print(Solution.numberOfSteps(0, 14))
