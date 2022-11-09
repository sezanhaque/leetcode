class Solution:
    def maximum69Number(self, num: int) -> int:
        s = str(num)
        left = 0

        while left < len(s) - 1 and s[left] == "9":
            left += 1

        if s[left] == "6":
            s = s[:left] + "9" + s[left + 1 :]

        return int(s)

    def maximum69Number(self, num: int) -> int:
        s = str(num)

        for i in range(len(s)):
            if s[i] != "9":
                s = s.replace("6", "9", 1)
                return int(s)

        return int(s)


print(Solution.maximum69Number(0, 9996))
print(Solution.maximum69Number(0, 9999))
