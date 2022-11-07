from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding Window

        count = Counter()
        res = left = maxF = 0

        for i in range(len(s)):
            count[s[i]] += 1
            maxF = max(maxF, count[s[i]])

            if i - left + 1 - maxF > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, i - left + 1)

        return res

    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()
        maxF = right = 0

        for i in range(len(s)):
            count[s[i]] += 1
            maxF = max(maxF, count[s[i]])

            if right - maxF < k:
                right += 1
            else:
                # subtract from the start to narrow down sliding window
                count[s[i - right]] -= 1

        return right


print(Solution.characterReplacement(0, s="ABAB", k=2))  # 4
print(Solution.characterReplacement(0, s="AABABBA", k=1))  # 4
print(Solution.characterReplacement(0, s="AABABBA", k=2))  # 5
print(Solution.characterReplacement(0, s="AABA", k=0))  # 2
print(Solution.characterReplacement(0, s="ABAA", k=0))  # 2
print(Solution.characterReplacement(0, s="AAAA", k=2))  # 4
print(Solution.characterReplacement(0, s="AAAA", k=0))  # 4
