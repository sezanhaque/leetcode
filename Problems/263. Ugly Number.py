class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for divisor in 2, 3, 5:
            while n % divisor == 0:
                n /= divisor
        return n == 1

    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 5 == 0:
            n /= 5
        while n % 3 == 0:
            n /= 3
        while n % 2 == 0:
            n /= 2
        return n == 1


if __name__ == "__main__":
    print(Solution.isUgly(0, 0))
