def myPow(self, x: float, n: int) -> float:
    """
    Time limit exceeded
    """
    limit = abs(n)
    result = 1

    for _ in range(limit):
        result *= x

    return result if n > -1 else 1 / result


def myPow(self, x: float, n: int) -> float:
    return x**n


def myPow(self, x: float, n: int) -> float:
    if n < 0:
        x = 1 / x
        n = -n
    power = 1

    while n:
        if n & 1:           # n % 2 != 0
            power *= x
        x *= x
        n >>= 1             # n //= 2
    return power

print(myPow(0, 2.00000, 10))
print(myPow(0, 2.10000, 3))
print(myPow(0, 2.00000, -2))
print(myPow(0, 34.00515, -3))
# print(myPow(0, 0.00001, 2147483647))
