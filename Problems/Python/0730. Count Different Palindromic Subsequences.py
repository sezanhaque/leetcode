from functools import cache, lru_cache
from typing import Set


class Solution:
    """
    Solution:

        1.  We traverse within a range, starting from 0 to end.

        2.  We will check if from current start to end if there is
            any "abcd" contains.
            If contains then we will get the range of them.

        3.  We can get many palindrome from the range if
            all condition passes.

    """
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        return self.generate(s, 0, len(s)) % MOD

    @cache
    def generate(self, s: str, start: int, end: int) -> int:
        # If start == end, it means we have exceeded our limit.
        if start >= end:
            return 0

        count = 0

        for char in "abcd":
            # get the left and right index of char from string
            left, right = s.find(char, start, end), s.rfind(char, start, end)

            # if these both are -1, it means there is no char in string
            if left == -1 or right == -1:
                continue

            # If left == right it means we are pointing same char
            # So we add 1
            if left == right:
                count += 1

            # Else we have found 2 char
            # So we add 2 and call next chars
            else:
                count += 2 + self.generate(s, left + 1, right)

        return count


obj = Solution()

print(obj.countPalindromicSubsequences("abccab"))
