class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []

        while columnNumber:
            columnNumber, reminder = divmod(columnNumber - 1, 26)
            ans.append(chr(reminder + ord("A")))

        return "".join(reversed(ans))


# print(Solution.convertToTitle(0, 1))
print(Solution.convertToTitle(0, 28))
