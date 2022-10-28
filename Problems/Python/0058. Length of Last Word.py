class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


# print(Solution.lengthOfLastWord(0, "Hello World"))
print(Solution.lengthOfLastWord(0, "   fly me   to   the moon  "))
