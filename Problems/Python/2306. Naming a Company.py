from collections import defaultdict
from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        res = 0
        wordSet = defaultdict(set)

        for word in ideas:
            wordSet[word[0]].add(word[1:])

        for a, set_a in wordSet.items():
            for b, set_b in wordSet.items():
                if a == b:
                    continue

                same = len(set_a & set_b)
                res += (len(set_a) - same) * (len(set_b) - same)

        return res


obj = Solution()
print(obj.distinctNames(["coffee", "donuts", "time", "toffee"]))
