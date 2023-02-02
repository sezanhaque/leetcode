from functools import cache


class Solution:
    @cache
    def tribonacci(self, n: int) -> int:
        if n < 0:
            return 0
        elif n < 2:
            return n

        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)


obj = Solution()
print(obj.tribonacci(25))
