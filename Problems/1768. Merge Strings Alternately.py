from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        for i, j in zip(word1, word2):
            ans = ans + i + j
        if len(word1) > len(word2):
            ans += word1[len(word2) :]
        else:
            ans += word2[len(word1) :]
        return ans

    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))


print(Solution.mergeAlternately(0, "ab", "pqrs"))
print(Solution.mergeAlternately(0, "abcd", "pq"))
print(Solution.mergeAlternately(0, "abc", "pqr"))
