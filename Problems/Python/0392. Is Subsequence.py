class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for val in s:
            idx = t.find(val)
            if idx == -1:
                return False
            else:
                t = t[idx + 1 :]

        return True

    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
            
        return i == len(s)


print(Solution.isSubsequence(0, "acb", "ahbgdc"))  # false
print(Solution.isSubsequence(0, "abc", "ahbgdc"))  # true
print(Solution.isSubsequence(0, "b", "c"))  # false
