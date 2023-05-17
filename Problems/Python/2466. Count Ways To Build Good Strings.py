from collections import Counter


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = Counter({0: 1})
        mod = 10 ** 9 + 7

        for i in range(1, high + 1):
            dp[i] = (dp[i - zero] + dp[i - one]) % mod

        return sum(dp[i] for i in range(low, high + 1)) % mod


obj = Solution()
print(obj.countGoodStrings(low=3, high=3, zero=1, one=1))
