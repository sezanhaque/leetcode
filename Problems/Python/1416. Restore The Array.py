class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        m, n = len(str(k)), len(s)
        dp = [1] * (n + 1)

        for i in range(n):
            res, curr = 0, ""

            for idx in range(i, max(-1, i - m), -1):
                curr = s[idx] + curr
                if curr[0] != "0" and int(curr) <= k:
                    res += dp[idx]

            if not res:
                return 0
            else:
                dp[i + 1] = res % (10 ** 9 + 7)

        return dp[-1]


obj = Solution()
print(obj.numberOfArrays(s="1000", k=10000))
