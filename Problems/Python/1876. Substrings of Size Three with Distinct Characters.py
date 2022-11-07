from collections import Counter


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        left, right = 0, 2

        while right < len(s):
            subStr = s[left : right + 1]
            strCount = Counter(subStr)
            if strCount[max(strCount, key=strCount.get)] == 1:
                count += 1
            left += 1
            right = left + 2
        return count

    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 2):
            subStr = s[i : i + 3]
            if len(set(subStr)) == 3:
                count += 1
        return count


print(Solution.countGoodSubstrings(0, "xyzzaz"))
print(Solution.countGoodSubstrings(0, "aababcabc"))
