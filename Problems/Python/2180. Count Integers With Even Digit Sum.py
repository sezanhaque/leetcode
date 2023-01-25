class Solution:
    def getDigitsSum(self, num) -> bool:
        res = 0

        while num:
            num, reminder = divmod(num, 10)
            res += reminder

        return True if not res & 1 else False

    def countEven(self, num: int) -> int:
        res = 0
        posInt = 2

        while posInt <= num:
            if posInt < 10:
                res += 1
                posInt += 2
            else:
                res += 1 if self.getDigitsSum(posInt) else 0
                posInt += 1
                
        return res


obj = Solution()
print(obj.countEven(30))
