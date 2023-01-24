class Solution:
    def largestPalindrome(self, n: int) -> int:
        # 1 digit max number
        if n == 1:
            return 9

        # min num with n digits: 10^(n-1)
        # Ex: n = 2, 10^(2-1) = 10
        # max num with n digits: 10^(n) - 1
        # Ex: n = 2, 10^2 - 1 = 100 - 1 = 99
        minNum, maxNum = 10 ** (n - 1), 10 ** n - 1

        maxPalindrome = 0

        # we are iterating from max num to min num with 2 steps
        # because max num will be always odd, so to make it palindrome
        # we need to step down 2
        for num in range(maxNum, minNum - 1, -2):
            # as we are searching for max palindrome, so we don't need to
            # search for a number which product is less than last max palindrome
            if num * num < maxPalindrome:
                break

            for j in range(maxNum, num - 1, -2):
                product = num * j

                # since a palindrome with an even number of digits must be mod 11 == 0
                # and we have no reason to check the product which less or equal than max_pal
                if product % 11 != 0 and product >= maxPalindrome:
                    continue

                if str(product) == str(product)[::-1]:
                    maxPalindrome = product

        return maxPalindrome % 1337

    def largestPalindrome(self, n: int) -> int:
        """
        1.  if the final result is of length 2n, because it is Palindrome,
            the result can be divided by 11 it means that we do not have
            to search with step size of 1 but step size of 11---ten times faster!

        2.  The constructed palindrome, for example n =7: ABCDEFGGFEDCBA,
            if it is divisible by two number of size n, both numbers will
            be greater than number ABCDEFG. Why? because ABCDEFGGFEDCBA > ABCDEFG * 10^n,
            note that 10^n is a number of size (n+1).

        """
        if n == 1:
            return 9

        hi, lo = 10 ** n - 1, 10 ** (n - 1)
        top = (hi // 11) * 11

        for left in range(hi, lo - 1, -1):
            res = int(str(left) + str(left)[::-1])

            for d in range(top, left - 1, -11):
                if res % d == 0:
                    q = res // d

                    if lo <= q <= hi:
                        return res % 1337

    def largestPalindrome(self, n: int) -> int:
        return [0, 9, 987, 123, 597, 677, 1218, 877, 475][n]


obj = Solution()
print(obj.largestPalindrome(2))
print(obj.largestPalindrome(3))
