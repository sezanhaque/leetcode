class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                if all(s[k].swapcase() in s[i:j] for k in range(i, j)):
                    ans = max(ans, s[i:j], key=len)
        return ans

    def longestNiceSubstring(self, s: str) -> str:
        ans = ""

        for i in range(len(s)):
            for j in range(i):
                subStr = s[j : i + 1]
                if set(subStr) == set(subStr.swapcase()):
                    ans = max(ans, subStr, key=len)
        return ans

    def longestNiceSubstring(self, s: str) -> str:
        # Fast
        for idx, val in enumerate(s):
            if val.swapcase() not in s:
                return max(
                    Solution.longestNiceSubstring(0, s[:idx]),
                    Solution.longestNiceSubstring(0, s[idx + 1 :]),
                    key=len,
                )
        return s


print(Solution.longestNiceSubstring(0, "YazaAay"))
# print(Solution.longestNiceSubstring(0, "aaA"))
