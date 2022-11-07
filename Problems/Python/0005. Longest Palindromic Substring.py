class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            odd = Solution.palindromeAt(0, s, i, i)
            even = Solution.palindromeAt(0, s, i, i + 1)

            res = max(res, odd, even, key=len)
        return res

    # starting at left, right expand outwards to find the biggest palindrome
    def palindromeAt(self, s: str, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]


print(Solution.longestPalindrome(0, "babad"))
print(Solution.longestPalindrome(0, "abacdfgdcaba"))
print(Solution.longestPalindrome(0, "abb"))
print(Solution.longestPalindrome(0, "ac"))
