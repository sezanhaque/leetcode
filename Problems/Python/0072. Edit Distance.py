from functools import cache


# Solution Link: https://leetcode.com/problems/edit-distance/solutions/1475220/python-3-solutions-top-down-dp-bottom-up-dp-o-n-in-space-clean-concise/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def DP(i: int, j: int):
            # Need to insert j chars
            if not i:
                return j
            # Need to delete i chars
            if not j:
                return i

            if word1[i - 1] == word2[j - 1]:
                return DP(i - 1, j - 1)

            # Choose the minimum cost among 3 operators
            # Delete: DP(i - 1, j) + 1
            # Insert: DP(i, j - 1) + 1
            # Replace: DP(i - 1, j - 1) + 1
            return min(DP(i - 1, j), DP(i, j - 1), DP(i - 1, j - 1)) + 1

        return DP(len(word1), len(word2))


obj = Solution()
print(obj.minDistance(word1="horse", word2="ros"))
