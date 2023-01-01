from typing import List


class Solution:
    """
    Nums will be between 2 - 1000.
    So, we only need to know the primes till square root of 1,000 which is 31.62...
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

    We will divide num from nums by these prime numbers and add them to a set.

    Lastly return the length of res set.
    """
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        res = set()

        for num in nums:
            for p in primes:
                if num % p == 0:
                    res.add(p)

                while num % p == 0:
                    num /= p

            # If the num is not 1 then it is the largest prime
            # after dividing the num by all primes
            if num != 1:
                res.add(num)

        return len(res)


obj = Solution()
print(obj.distinctPrimeFactors([2, 4, 3, 7, 10, 6]))
