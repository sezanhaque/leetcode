from functools import cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        If we get the longest common subsequence between
        string s and reversed s then this will be the ans.
        """
        return Solution.helper(0, s, s[::-1], 0, 0)

    @cache
    def helper(self, text1: str, text2: str, i: int, j: int) -> int:
        """
        Leetcode 1143 Longest Common Subsequence problem
        """
        if i >= len(text1) or j >= len(text2):
            return 0

        if text1[i] == text2[j]:
            return 1 + Solution.helper(0, text1, text2, i + 1, j + 1)
        else:
            return max(
                Solution.helper(0, text1, text2, i + 1, j),
                Solution.helper(0, text1, text2, i, j + 1),
            )

    def longestPalindromeSubseq(self, s: str) -> int:
        # fast
        @cache
        def helper(i, j):
            # if i == j then it means
            # there is only one char
            # and one char can be a palindrome
            if i == j:
                return 1

            if j < i:
                return 0

            # if s[i] == s[j] it means
            # we have found 2 char which are same
            # so together these will be palindrome
            if s[i] == s[j]:
                return 2 + helper(i + 1, j - 1)
            else:
                return max(helper(i, j - 1), helper(i + 1, j))

        return helper(0, len(s) - 1)


print(Solution.longestPalindromeSubseq(0, "bbbab"))
