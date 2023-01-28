class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Time Limit Exceeded
        limit = n ** 0.5

        for i in range(int(limit.real) + 1):
            if 3 ** i == n:
                return True

        return False

    def isPowerOfThree(self, n: int) -> bool:
        """
        The positive divisors of 3^19 are exactly the powers of 3 from 3^0 to 3^19.
        That's all powers of 3 in the possible range here (signed 32-bit integer).
        So just check whether the number is positive and whether it divides 3^19.
        """
        return n > 0 == 3 ** 19 % n


obj = Solution()
print(obj.isPowerOfThree(3))
