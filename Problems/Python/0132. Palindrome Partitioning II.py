from functools import cache
from math import inf


class Solution:
    def minCut(self, s: str) -> int:
        @cache
        def isPalindrome(start: int, end: int) -> bool:
            if start >= end:
                return True

            if s[start] != s[end]:
                return False

            return isPalindrome(start + 1, end - 1)

            # this will slow the speed
            # return s[start:end] == s[start:end][::-1]

        @cache
        def DP(idx: int) -> int:
            if idx == len(s):
                return 0

            res = inf

            # iterate through idx to len(s)
            # to check if the range is palindrome
            # if so then go to the next idx and add 1 as cut
            for j in range(idx, len(s)):
                if isPalindrome(idx, j):
                    res = min(res, DP(j + 1) + 1)

            return res

        # in the end we will go to the last of string,
        # and it will also count as a cut, so we are
        # subtracting it
        return DP(0) - 1


obj = Solution()
print(obj.minCut("aab"))
print(obj.minCut("abcbdd"))
