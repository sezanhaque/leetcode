from functools import cache


class Solution:
    @cache
    def uniquePaths(self, m: int, n: int) -> int:
        # if we are on the edge of bottom / right
        # it means now we have only one way to reach bottom-right corner.
        # this is why we are returning 1
        if m == 1 or n == 1:
            return 1

        # going to right: col - 1
        right = self.uniquePaths(m, n - 1)

        # going to bottom: row - 1
        bottom = self.uniquePaths(m - 1, n)

        return right + bottom


obj = Solution()
print(obj.uniquePaths(m=23, n=12))
