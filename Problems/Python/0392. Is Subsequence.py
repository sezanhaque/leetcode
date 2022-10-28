class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for val in s:
            idx = t.find(val)
            if idx == -1:
                return False
            else:
                t = t[idx + 1 :]

        return True


print(Solution.isSubsequence(0, "acb", "ahbgdc"))  # false
print(Solution.isSubsequence(0, "abc", "ahbgdc"))  # true
print(Solution.isSubsequence(0, "b", "c"))  # false
