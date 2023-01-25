import math


class Solution:
    def isHappy(self, n: int) -> bool:
        """
        If n == 1 then loop will be executed
        But while n != 1 the calculation will be looped
        So we are storing every n in seen so that when
        we find the same value, we can assure that there
        will be n == 1
        """
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = self.getSum(self.getNumbers(n))

        # if n == 1 then loop will be executed before 
        # it stores to seen
        # if n != 1 then n will be in seen
        return n not in seen

    def getSum(self, nums: list[int]) -> int:
        """
        Get sum of every square of digits of the number
        """
        sums = 0
        for num in nums:
            sums += math.pow(num, 2)
        return sums

    def getNumbers(self, num: int) -> list[int]:
        """
        Get the digits of the number
        """
        result = []
        while num != 0:
            num, reminder = divmod(num, 10)
            result.append(reminder)
        return result


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = self.findSquare(n)

        return n not in seen

    def findSquare(self, num: int) -> int:
        res = 0

        while num:
            num, reminder = divmod(num, 10)
            res += reminder * reminder

        return res

    def isHappy(self, n: int) -> bool:
        # Using Linked list cycle detection method
        slow = fast = n

        while True:
            slow = self.findSquare(slow)
            fast = self.findSquare(self.findSquare(fast))
            if slow == fast:
                break

        return True if slow == 1 else False


obj = Solution()
print(obj.isHappy(19))
print(obj.isHappy(2))
