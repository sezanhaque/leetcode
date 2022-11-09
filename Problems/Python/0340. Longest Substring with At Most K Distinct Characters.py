from collections import Counter


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # Premium
        # Sliding Window
        count = Counter()
        left = ans = 0

        for i in range(len(s)):
            count[s[i]] += 1

            while len(count) > k:
                if count[s[left]] == 1:
                    del count[s[left]]
                else:
                    count[s[left]] -= 1
                left += 1
            ans = max(ans, i - left + 1)

        return ans


print(Solution.lengthOfLongestSubstringKDistinct(0, "eceba", 2))
print(Solution.lengthOfLongestSubstringKDistinct(0, "aa", 1))
