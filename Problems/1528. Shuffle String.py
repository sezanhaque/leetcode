class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        ans = [""] * len(s)
        for i in range(len(s)):
            ans[indices[i]] = s[i]
        return "".join(ans)


print(Solution.restoreString(0, "codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
print(Solution.restoreString(0, "abc", [0, 1, 2]))
