class Solution:
    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        def check(word1: str, word2: str) -> bool:
            # Check how many different character are between word1 & word2
            # Return True if difference is <= 2
            return sum(1 for i, j in zip(word1, word2) if i != j) <= 2

        ans = []

        for q in queries:
            for d in dictionary:
                if check(q, d):
                    ans.append(q)
                    break

        return ans

    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        return [
            q
            for q in queries
            if any(sum(i != j for i, j in zip(q, d)) <= 2 for d in dictionary)
        ]


print(
    Solution.twoEditWords(0, ["word", "note", "ants", "wood"], ["wood", "joke", "moat"])
)
