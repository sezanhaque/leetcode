from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = "aeiou"
        res = 0

        for idx in range(left, right + 1):
            res += words[idx][0] in vowels and words[idx][-1] in vowels

        return res


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = "aeiou"

        return sum(words[idx][0] in vowels and words[idx][-1]
                   in vowels for idx in range(left, right + 1))


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        return sum({w[0], w[-1]} < {'a', 'e', 'i', 'o', 'u'} for w in words[left: right + 1])


obj = Solution()
print(obj.vowelStrings(words=["are", "amy", "u"], left=0, right=2))
