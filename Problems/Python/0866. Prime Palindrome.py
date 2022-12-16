class Solution:
    # Fast
    def primePalindrome(self, n: int) -> int:
        if 8 <= n <= 11:
            return 11

        for i in range(10 ** (len(str(n)) >> 1), 10**5):
            # eg. s = '123' to i = int('12321')
            palindrome = int(str(i) + str(i)[-2::-1])
            if palindrome >= n and Solution.isPrime(0, palindrome):
                return palindrome

    def isPrime(self, num: int) -> bool:
        return num > 1 and all(num % i for i in range(2, int(num**0.5) + 1))


class Solution:
    def primePalindrome(self, n: int) -> int:
        while True:
            if Solution.isPalindrome(0, n) and Solution.isPrime(0, n):
                return n
            n += 1

            # Any even length palindrome must be divisble by 11
            # so we will skip numbers N = [10,000,000, 99,999,999]
            if 10**7 < n < 10**8:
                n = 10**8

    def isPrime(self, num: int) -> bool:
        return num > 1 and all(num % i for i in range(2, int(num**0.5) + 1))

    def reverseNumber(self, num: int) -> int:
        res = 0
        while num:
            res = 10 * res + num % 10
            num //= 10
        return res

    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

print(Solution.primePalindrome(0, 9989900))
