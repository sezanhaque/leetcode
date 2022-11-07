import re


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        left, right = 0, len(s) - 1
        s = list(s)

        while left < right:
            while s[left] not in vowels and left < right:
                left += 1
            while s[right] not in vowels and left < right:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return "".join(s)

    def reverseVowels(self, s: str) -> str:
        vowels = (c for c in reversed(s) if c in "aeiouAEIOU")
        return re.sub("(?i)[aeiou]", lambda a: next(vowels), s)

    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}
        vowlesInS = [c for c in s if c in vowels]

        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = vowlesInS.pop(-1)

        return "".join(s)


print(Solution.reverseVowels(0, "hello"))
print(Solution.reverseVowels(0, "leetcode"))
print(Solution.reverseVowels(0, "A man, a plan, a canal: Panama"))
