import collections


class Solution:
    def oddString(self, words: list[str]) -> str:
        def calculateDifference(word: str) -> tuple:
            # Calculate Difference between i and i + 1 of the word
            return tuple(ord(word[i + 1]) - ord(word[i]) for i in range(len(word) - 1))

        differenceDict = collections.defaultdict(int)

        for word in words:
            # Store the difference of the words into the hashmap
            # and their occurrences.
            differenceDict[calculateDifference(word)] += 1

        for word in words:
            # Find the word which occurred once.
            if differenceDict[calculateDifference(word)] == 1:
                return word


print(Solution.oddString(0, ["adc", "wzy", "abc"]))
