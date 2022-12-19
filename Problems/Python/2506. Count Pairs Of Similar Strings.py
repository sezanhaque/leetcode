from collections import defaultdict


class Solution:
    def similarPairs(self, words: list[str]) -> int:
        res = 0

        for idx, word1 in enumerate(words):
            for word2 in words[idx + 1 :]:
                res += set(word1) == set(word2)

        return res

    def similarPairs(self, words: list[str]) -> int:
        return sum(
            set(word1) == set(word2)
            for idx, word1 in enumerate(words)
            for word2 in words[idx + 1 :]
        )

    def similarPairs(self, words: list[str]) -> int:
        dict, res = defaultdict(int), 0

        for word in words:
            n = 0
            for char in word:
                n |= 1 << ord(char) - ord("a")
            dict[n] += 1

        for char in dict.values():
            res += (char * (char - 1)) >> 1

        return res


print(Solution.similarPairs(0, ["aba", "aabb", "abcd", "bac", "aabc"]))  # 2
# print(Solution.similarPairs(0, ["aabb", "ab", "ba"]))  # 3
# print(Solution.similarPairs(0, ["nba", "cba", "dba"]))  # 0
