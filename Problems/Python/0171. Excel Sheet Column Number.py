class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for letter in columnTitle:
            res = res * 26 + (ord(letter) - 64)
        return res

    def titleToNumber(self, columnTitle: str) -> int:
        """
        In base 10, the digit value in each position is 1, 10, 100, 1000…
        In base 26, like here, the digit value in each position is 1, 26, 676, 17576…
        which corresponds to 26^0 = 1, 26^1 = 26, 26^2 = 676, 26^3 = 17576…
        """
        res = 0
        for idx, val in enumerate(columnTitle[::-1]):
            res += 26**idx * (ord(val) - 64)
        return res


print(Solution.titleToNumber(0, "AB"))  # 28
