from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Backtracking solution

        # create a set from wordDict so we can iterate fast
        words_set = frozenset(wordDict)
        res = []

        def Backtrack(start: int, path: List):
            if start == len(s):
                res.append(" ".join(path))
                return

            for end in range(start, len(s)):
                currStr = s[start: end + 1]
                if not s[start: end + 1] in words_set:
                    continue

                path.append(s[start: end + 1])
                Backtrack(end + 1, path)
                path.pop()

        Backtrack(0, [])
        return res

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # DP solution

        # create a set from wordDict so we can iterate fast
        words_set = frozenset(wordDict)

        @cache
        def DP(idx: int) -> List[str]:
            res = []

            for word in words_set:
                if word != s[idx:idx + len(word)]:
                    continue
                # if we reach the last word of the string
                elif len(word) == len(s) - idx:
                    res.append(word)
                else:
                    for sentence in DP(idx + len(word)):
                        res.append(word + ' ' + sentence)
            return res

        return DP(0)

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Fast

        memo = {len(s): ['']}

        # create a set from wordDict so we can iterate fast
        words_set = frozenset(wordDict)

        # length list of words from words_set
        # we just need to iterate from these range
        len_w = set(len(w) for w in words_set)

        def sentences(idx) -> List[str]:
            if idx not in memo:
                memo[idx] = [s[idx:idx + j] + (tail and ' ' + tail)
                             for j in len_w
                             if s[idx:idx + j] in words_set
                             for tail in sentences(idx + j)]
            return memo[idx]

        return sentences(0)


obj = Solution()
print(obj.wordBreak(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"]))
