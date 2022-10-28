class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]

    def reverseString(self, s: list[str]) -> None:
        for i in range(len(s) >> 1):
            # "~i" is same as "- i - 1"
            s[i], s[~i] = s[~i], s[i]
        return s


print(Solution.reverseString(0, ["h", "e", "l", "l", "o"]))
