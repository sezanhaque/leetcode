from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        for val, occurrence in Counter(s).items():
            if occurrence == 1:
                return s.index(val)
        return -1


obj = Solution()
print(obj.firstUniqChar("leetcode"))
