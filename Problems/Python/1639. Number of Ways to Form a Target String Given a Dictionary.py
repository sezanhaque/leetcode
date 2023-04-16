from collections import Counter
from functools import cache
from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        # bottom-up approach

        res = [1] + [0] * len(target)

        for idx in range(len(words[0])):
            cnt = Counter(word[idx] for word in words)

            for j in range(min(idx + 1, len(target)), 0, -1):
                res[j] = (res[j] + res[j - 1] * cnt[target[j - 1]]) % (10 ** 9 + 7)

        return res[len(target)]

    def numWays(self, words: List[str], target: str) -> int:
        # top-down approach
        cnt = [Counter(w[idx] for w in words) for idx in range(len(words[0]))]

        @cache
        def DFS(i: int, j: int) -> int:
            if j >= len(target):
                return 1

            k = len(cnt) - len(target) + j + 1

            return sum(cnt[k][target[j]] * DFS(k + 1, j + 1) for k in range(i, k)) % (10 ** 9 + 7)

        return DFS(0, 0)


obj = Solution()
print(obj.numWays(words=["acca", "bbbb", "caca"], target="aba"))
