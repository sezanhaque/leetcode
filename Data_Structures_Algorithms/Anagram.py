from collections import defaultdict, Counter
from itertools import groupby
from typing import List, Any


class Anagram:
    def is_anagram(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        return Counter(word1) == Counter(word2)

    def group_anagrams_groupby(self, words: List) -> list[list[Any]]:
        return [list(group) for key, group in groupby(sorted(words, key=sorted), sorted)]

    def group_anagrams(self, words: list) -> list[List[str]]:
        # fast
        res = defaultdict(list)

        for word in words:
            res[tuple(sorted(word))].append(word)

        return list(res.values())


obj = Anagram()
words = ['abc', 'cab', 'cafe', 'goo', 'face']
print(obj.is_anagram("abc", "cba"))
print(obj.group_anagrams_groupby(words))
print(obj.group_anagrams(words))
