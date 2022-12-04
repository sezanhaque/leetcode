from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        1.  Operation 1 allows us to swap any two symbols, so what matters in the end not order of them,
            but how many of each symbol we have. Imagine we have (6, 3, 3, 5, 6, 6) frequencies of symbols,
            than we need to have the same frequencies for the second string as well. So, we need to check
            if we have the same elements, but in different order (that is one is anagrams of another),
            how we can efficiently check it? We can sort both of them and compare, or we can use
            Counter again to check if these two lists have the same elements! Yes, we use here Counter
            of Counter and to be honest I see it first time, but it is not that difficult.


        2.  Operation 2 allows us to rename our letters, but we need to use the same letters: it means,
            that set of letters in first and second strings should be the same.

        Complexity:
        Time complexity is O(n), we create counters, and then again create counters.
        Space complexity is O(m), where m is size of alphabet to keep our counters.
        """

        return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(
            Counter(word2).values()
        )


print(Solution.closeStrings(0, word1="abc", word2="bca"))
print(Solution.closeStrings(0, word1="a", word2="aa"))
