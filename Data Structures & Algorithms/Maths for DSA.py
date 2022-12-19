import math


def isPrime(num: int) -> bool:
    """
    A Prime number is only divisible by itself and 1.

    If the number is divisible from 2 to its square root
    then this will not be a prime number.
    """
    return num > 1 and all(num % i for i in range(2, int(num**0.5) + 1))


# print("*" * 20 + "Prime Number" + "*" * 20)
# print(isPrime(36))
# print("*" * 20 + "Prime Number" + "*" * 20 + "\n\n")


def SieveOfEratosthenes(num: int) -> None:
    """
    Python program to print all
    primes smaller than or equal to
    n using Sieve of Eratosthenes
    """
    primes = [True] * (num + 1)

    for i in range(2, int(num**0.5) + 1):
        # If i is true then it is prime
        if primes[i]:
            # Update all multiple of i
            for j in range(i * i, num + 1, i):
                primes[j] = False

    print("Following are the prime numbers smaller than or equal to", num)
    for i in range(2, num + 1):
        if primes[i]:
            print(i, end=" ")


# print("*" * 20 + "Sieve Of Eratosthenes" + "*" * 20)
# print(SieveOfEratosthenes(10))
# print("*" * 20 + "Sieve Of Eratosthenes" + "*" * 20 + "\n\n")


def primeFactors(num: int) -> list[int]:
    """
    Prime factor of a number
    """
    res = []
    c = 2
    while num > 1:
        if num % c == 0:
            res.append(c)
            num = num // c
        else:
            c = c + 1
    return res


# print("*" * 20 + "Prime Factors of a number" + "*" * 20)
# print(primeFactors(100))
# print("*" * 20 + "Prime Factors of a number" + "*" * 20 + "\n\n")


class Prime_Factor_Sieve_Of_Eratosthenes:
    """
    Prime Factorization using Sieve O(log n) for multiple queries
    """

    def __init__(self) -> None:
        self.max_num = 10**5 + 1

        # stores the smallest prime factor
        # for every number
        self.spf = [0] * self.max_num

    # Calculating SPF (The smallest Prime Factor)
    # for every number till max_num.
    # Time Complexity : O(n log)
    def sieve(self):
        self.spf[1] = 1
        for i in range(2, self.max_num):

            # marking the smallest prime factor
            # for every number to be itself.
            self.spf[i] = i

        # separately marking spf for
        # every even number as 2
        for i in range(4, self.max_num, 2):
            self.spf[i] = 2

        for i in range(3, math.ceil(math.sqrt(self.max_num))):

            # checking if i is prime
            if self.spf[i] == i:

                # marking SPF for all numbers
                # divisible by i
                for j in range(i * i, self.max_num, i):

                    # marking spf[j] if it is
                    # not previously marked
                    if self.spf[j] == j:
                        self.spf[j] = i

    # A O(log n) function returning prime
    # factorization by dividing by smallest
    # prime factor at every step
    def getFactorization(self, num: int) -> list[int]:
        res = []
        while num != 1:
            res.append(self.spf[num])
            num = num // self.spf[num]

        return res


# print(
#     "*" * 20
#     + "Prime Factorization using Sieve O(log n) for multiple queries"
#     + "*" * 20
# )
# initialize = Prime_Factor_Sieve_Of_Eratosthenes()
# initialize.sieve()
# print(initialize.getFactorization(100000))
# print(
#     "*" * 20
#     + "Prime Factorization using Sieve O(log n) for multiple queries"
#     + "*" * 20
#     + "\n\n"
# )


def reverseNumber(num: int) -> int:
    """
    Reverse a number.
    Ex: 23 -> 32
    """
    res = 0
    while num:
        res = 10 * res + num % 10
        num //= 10
    return res


# print("*" * 20 + "Reverse a number" + "*" * 20)
# print(reverseNumber(23))
# print("*" * 20 + "Reverse a number" + "*" * 20 + "\n\n")


def gcd(a: int, b: int) -> int:
    """
    Greatest common divisor (GCD) or
    Highest common factor (HCF)
    Using Euclidean algorithm

    GCD of a, b = GCD of b%a, a
    """
    if a == 0:
        return b
    return gcd(b % a, a)


# print("*" * 20 + "GCD | HCF" + "*" * 20)
# print(gcd(4, 17))
# print("*" * 20 + "GCD | HCF" + "*" * 20 + "\n\n")


def lcm(a: int, b: int) -> int:
    """
    LCM is the short form for “Least Common Multiple.”

    The least common multiple is defined as the smallest
    multiple that two or more numbers have in common.

    LCM of a, b = (a * b) // GCD of a, b

    Therefore, we also can say that
    Multiplication of two numbers are multiplication of their LCM & GCD.
    """
    return (a * b) // gcd(a, b)


# print("*" * 20 + "Least common multiple" + "*" * 20)
# print(lcm(4, 17))
# print("*" * 20 + "Least common multiple" + "*" * 20 + "\n\n")
