from functools import lru_cache


class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        res = 0

        for i in range(length):
            for j in range(i, length):
                if self.isPalindrome(s[i: j + 1]):
                    res += 1
        return res

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]


obj = Solution()
print(obj.countSubstrings("abc"))


class Solution:
    def countSubstrings(self, s: str) -> int:
        # using recursion
        length = len(s)
        res = 0

        @lru_cache(None)
        def isPalindrome(left, right):
            if left > right:
                return True
            if s[left] != s[right]:
                return False
            return isPalindrome(left + 1, right - 1)

        for i in range(length):
            for j in range(i, length):
                if isPalindrome(i, j):
                    res += 1
        return res


class Solution:
    """
    Faster
    Link: https://leetcode.com/problems/palindromic-substrings/solutions/1129426/js-python-java-c-optimized-mathematical-solution-w-explanation/
    """

    def countSubstrings(self, s: str) -> int:
        ans, left, right = 0, 0, len(s)

        while left < right:
            i, j = left - 1, left

            while j < right - 1 and s[j] == s[j + 1]:
                j += 1
            ans += ((j - i) * (j - i + 1)) >> 1
            left, j = j + 1, j + 1

            while ~i and j < right and s[j] == s[i]:
                i, j, ans = i - 1, j + 1, ans + 1

        return ans


class Solution:
    # NeetCode solution
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.countPalindrome(s, i, i)
            res += self.countPalindrome(s, i, i + 1)

        return res

    def countPalindrome(self, s: str, left: int, right: int) -> int:
        res = 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            res += 1
            left -= 1
            right += 1

        return res


obj = Solution()

print(obj.countSubstrings("abc"))
