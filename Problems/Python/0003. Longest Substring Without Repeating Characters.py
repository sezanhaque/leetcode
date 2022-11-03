class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window
        ans = 0
        curr = ""
        for val in s:
            if val not in curr:
                curr += val
                ans = max(ans, len(curr))
            else:
                curr = curr[curr.index(val) + 1 :] + val
        return ans

    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = ans = 0

        for idx, val in enumerate(s):
            while val in seen:
                seen.remove(s[left])
                left += 1
            seen.add(val)
            ans = max(ans, idx - left + 1)
            
        return ans

    def lengthOfLongestSubstring(self, s: str) -> int:
        # Official Solution from LeetCode
        chars = [None] * 128

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]

            index = chars[ord(r)]
            if index is not None and left <= index < right:
                left = index + 1

            res = max(res, right - left + 1)

            chars[ord(r)] = right
            right += 1
        return res


print(Solution.lengthOfLongestSubstring(0, "abcabcbb"))
print(Solution.lengthOfLongestSubstring(0, "pwwkew"))
