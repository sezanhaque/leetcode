class Solution:
    def getDigitsSum(self, num) -> int:
        res = 0

        while num:
            num, reminder = divmod(num, 10)
            res += reminder

        return res

    def getLucky(self, s: str, k: int) -> int:
        res = 0

        for char in s:
            num = ord(char) - 96
            res += self.getDigitsSum(num)

        while k > 1:
            res = self.getDigitsSum(res)
            k -= 1

        return res


obj = Solution()
print(obj.getLucky(s="leetcode", k=2))
