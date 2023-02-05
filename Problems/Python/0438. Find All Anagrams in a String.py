from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        p = sorted(p)
        p_len = len(p)

        for idx in range(len(s) - p_len + 1):
            if sorted(s[idx: idx + p_len]) == p:
                res.append(idx)

        return res

    def findAnagrams(self, s: str, p: str) -> List[int]:
        # sliding window
        res = []
        left = 0
        counter = Counter(p)

        for right, char in enumerate(s):
            counter[char] -= 1

            # while there is more than our expected char
            # we move from left to right
            while counter[char] < 0:
                # slide from left to right
                counter[s[left]] += 1
                left += 1

            # if the distance between left and right pointer
            # is equal to the length of p it means we have found
            # one ans
            if right - left + 1 == len(p):
                res.append(left)

        return res


obj = Solution()
print(obj.findAnagrams(s="cbaebabacd", p="abc"))
print(obj.findAnagrams(s="abab", p="ab"))
