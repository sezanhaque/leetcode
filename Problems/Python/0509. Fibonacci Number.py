from functools import cache


class Solution:
    def fib(self, n: int) -> int:
        self.seen = {}
        return self.helper(n)

    def helper(self, num: int) -> int:
        if num < 0:
            return
        elif num < 2:
            return num
        elif num in self.seen:
            return self.seen[num]
        self.seen[num] = self.helper(num - 1) + self.helper(num - 2)
        return self.seen[num]


    def fib(self, n: int) -> int:
        golden_ratio = (1 + 5 ** 0.5) / 2
        return int((golden_ratio ** n + 1) / 5 ** 0.5)

    @cache
    def fib(self, num: int) -> int:
        if num < 0:
            return
        elif num < 2:
            return num
        return self.fib(num - 1) + self.fib(num - 2)

print(Solution.fib(0, 29))