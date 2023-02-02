import itertools
from typing import List, Dict


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map: Dict[int] = {val: idx for idx, val in enumerate(order)}

        for w1, w2 in zip(words, words[1:]):
            for i, j in zip(w1, w2):
                if i != j:
                    if order_map[i] > order_map[j]:
                        return False
                    # if we find the first different character, and they are sorted,
                    # then there's no need to check remaining letters
                    break
            # if a part of w1 is w2 but w1 != w2
            # it means there will be some left over
            # which is not sorted with w2
            if w1.startswith(w2) and w1 != w2:
                return False

        return True

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map: Dict[int] = {val: idx for idx, val in enumerate(order)}

        def compare(a: str, b: str) -> bool:
            for char1, char2 in zip(a, b):
                if char1 != char2:
                    return order_map[char1] < order_map[char2]
            return len(a) <= len(b)

        return all(compare(w1, w2) for w1, w2 in itertools.pairwise(words))


obj = Solution()
print(obj.isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"))
print(obj.isAlienSorted(words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz"))
print(obj.isAlienSorted(words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz"))
