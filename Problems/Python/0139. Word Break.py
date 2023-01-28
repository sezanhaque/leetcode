from functools import cache
from typing import List, FrozenSet


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DFS with Memoization + HashSet

        # create a set from wordDict so we can iterate fast
        words_set = frozenset(wordDict)

        @cache
        def DFS(start: int) -> bool:
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if s[start:end] in words_set and DFS(end):
                    return True

            return False

        return DFS(0)

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP
        DP = [False] * (len(s) + 1)
        DP[0] = True

        words_set = frozenset(wordDict)
        word_max_len = len(max(wordDict, key=len)) if wordDict else 0

        for idx in range(1, len(s) + 1):
            for j in range(max(0, idx - word_max_len), idx):
                if DP[j] and s[j:idx] in words_set:
                    DP[idx] = True
                    break

        return DP[-1]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP sort form
        DP = [True]
        words_set = frozenset(wordDict)
        word_max_len = len(max(wordDict, key=len)) if wordDict else 0

        for idx in range(1, len(s) + 1):
            DP += [any(DP[j] and s[j:idx] in words_set for j in range(max(0, idx - word_max_len), idx))]

        return DP[-1]


obj = Solution()
print(obj.wordBreak(s="leetcode", wordDict=["leet", "code"]))
print(obj.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
