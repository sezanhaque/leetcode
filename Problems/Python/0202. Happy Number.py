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
            n = Solution.getSum(0, Solution.getNumbers(0, n))

        # if n == 1 then loop will be executed before 
        # it stores to seen
        # if n != 1 then n will be in seen
        return n not in seen

    def getSum(self, nums: list[int]) -> int:
        """
        Get sum of every square of digits of the number
        """
        sums = 0
        for i in nums:
            sums += math.pow(i, 2)
        return sums

    def getNumbers(self, n: int) -> list[int]:
        """
        Get the digits of the number
        """
        result = []
        while n != 0:
            n, reminder = divmod(n, 10)
            result.append(reminder)
        return result


print(Solution.isHappy(0, 19))
print(Solution.isHappy(0, 2))
