from functools import cache


class Solution:
    """
    The answer will be a recursive sequence as follow: 1, 1, 2, 5, 11, 24, 53, 117, 258, 569, 1255
    It grows at a speed about 2 times bigger each time.
    If you write down this recursive sequence and do some calculations, you may find that:

    5 = 2 * 2 + 1
    11 = 5 * 2 + 1
    24 = 11 * 2 + 2
    53 = 24 * 2 + 5
    117 = 53 * 2 + 11

    A[n] = 2 * A[n-1] + A[n-3]
    """

    def numTilings(self, n: int) -> int:
        # Using recursion

        MOD = 10 ** 9 + 7

        @cache
        def solve(n: int) -> int:
            if n < 3:
                return n
            if n == 3:
                return 5

            return 2 * solve(n - 1) + solve(n - 3)

        return solve(n) % MOD

    def numTilings(self, n):
        a, b, c = 0, 1, 1

        for i in range(n - 1):
            a, b, c = b, c, (c + c + a)

        return c % int(1e9 + 7)


obj = Solution()
print(obj.numTilings(3))
