class Solution:
    def smallestValue(self, n: int) -> int:
        while n != (n := Solution.primes(0, n)):
            pass
        return n

    def primes(self, num: int, res: int = 0) -> int:
        for i in range(2, num + 1):
            while num % i == 0:
                res += i
                num //= i

            if i >= num:
                return res


print(Solution.smallestValue(0, 15))
