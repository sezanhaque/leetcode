class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


print(Solution.reverseWords(0, "the sky is blue"))
print(Solution.reverseWords(0, "  hello world  "))
print(Solution.reverseWords(0, "a good   example"))
