class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = [""] * numRows
        idx = 0
        backward = True

        for char in s:
            res[idx] += char

            # if we are at the top or bottom
            if idx == 0 or idx == numRows - 1:
                backward = not backward

            # if we are on backward
            if backward:
                idx -= 1
            else:
                idx += 1

        return "".join(res)


obj = Solution()
print(obj.convert(s="PAYPALISHIRING", numRows=3))
