from collections import Counter


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        seen, result = set(), set()

        for i in range(len(s) - 9):
            current = s[i : i + 10]
            if current in seen:
                result.add(current)
            else:
                seen.add(current)
        return list(result)

    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        count = Counter((s[i : i + 10] for i in range(len(s) - 9)))

        # using generator, fast
        return  (idx for idx in count if count[idx] > 1)

        # using list
        return  [idx for idx in count if count[idx] > 1]


print(Solution.findRepeatedDnaSequences(0, "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
