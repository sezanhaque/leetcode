class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            sums = 0
            while num:
                num, reminder = divmod(num, 10)
                sums += reminder
            num = sums

        return num

    def addDigits(self, num: int) -> int:
        """
        The original number is divisible by 9 if and only if the sum of its digits is divisible by 9.
        """
        # if num == 0
        if not num:
            return 0
        # if num % 9 == 0
        if not num % 9:
            return 9
        # else return the answer of num % 9
        return num % 9


obj = Solution()
print(obj.addDigits(38))
print(ord("a") - 96)