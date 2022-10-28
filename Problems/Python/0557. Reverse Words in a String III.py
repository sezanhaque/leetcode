class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([i[::-1] for i in s.split()])


print(Solution.reverseWords(0, "Let's take LeetCode contest"))
print(Solution.reverseWords(0, "God Ding"))
