class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        return "".join(word1) == "".join(word2)


print(Solution.arrayStringsAreEqual(0, ["ab", "c"], ["a", "bc"]))
print(Solution.arrayStringsAreEqual(0, ["a", "cb"], ["ab", "c"]))
print(Solution.arrayStringsAreEqual(0, ["abc", "d", "defg"], ["abcddefg"]))
