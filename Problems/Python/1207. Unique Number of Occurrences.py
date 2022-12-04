from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        """
        Count the number of occurrences
        Count the unique number of occurrences using set
        """
        return len(count := Counter(arr)) == len(set(count.values()))


print(Solution.uniqueOccurrences(0, [1, 2, 2, 1, 1, 3]))
