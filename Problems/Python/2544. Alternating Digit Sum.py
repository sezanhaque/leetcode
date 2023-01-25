class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res = 0
        step = 1

        for num in str(n):
            res += step * int(num)
            step *= -1

        return res


obj = Solution()
print(obj.alternateDigitSum(521))
print(obj.alternateDigitSum(10))  # 1
print(obj.alternateDigitSum(25))  # -3
