class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        """
        If n is even then it will be divisible by 2.
        If n is odd then its double will be divisible by 2.
        
        n & 1 => detects if it is even or odd.
        If n is even then it will return 0, otherwise 1.

        If we left shift by 0 then the number will be same.
        If we left shift by 1 then it will actually multiply by 2.
        """
        return n << (n & 1)


print(Solution.smallestEvenMultiple(0, 5))
print(Solution.smallestEvenMultiple(0, 6))
