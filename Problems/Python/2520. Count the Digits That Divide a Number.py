class Solution:
    def countDigits(self, num: int) -> int:
        length = num
        res = 0

        while length > 0:
            length, div = divmod(length, 10)
            if num % div == 0:
                res += 1

        return res

    def countDigits(self, num: int) -> int:
        return sum(num % int(d) == 0 for d in str(num))


obj = Solution()
print(obj.countDigits(121))
