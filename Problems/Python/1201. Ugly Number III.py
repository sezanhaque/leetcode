from math import gcd

# https://leetcode.com/problems/ugly-number-iii/solutions/387539/cpp-Binary-Search-with-picture-and-Binary-Search-Template/


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def enough() -> bool:
            total = (
                mid // a
                + mid // b
                + mid // c
                - mid // ab
                - mid // ac
                - mid // bc
                + mid // abc
            )
            return total >= n

        ab = a * b // gcd(a, b)
        ac = a * c // gcd(a, c)
        bc = b * c // gcd(b, c)
        abc = a * bc // gcd(a, bc)

        left, right = 1, 10**10

        while left < right:
            mid = left + ((right - left) >> 1)

            if enough():
                right = mid
            else:
                left = mid + 1
        return left


print(Solution.nthUglyNumber(0, 3, 2, 3, 5))
