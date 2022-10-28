import collections
from functools import reduce


def hasGroupsSizeX(self, deck: list[int]) -> bool:
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    count = collections.Counter(deck).values()
    return reduce(gcd, count) > 1


def hasGroupsSizeX(self, deck: list[int]) -> bool:
    count = collections.Counter(deck).values()
    minimum = min(count)

    if minimum < 2:
        return False
    for i in range(minimum, 1, -1):
        result = all(value % i == 0 for value in count)
        if result:
            return True
    return False


# print(hasGroupsSizeX(0, [1, 1, 1, 2, 2, 2, 3, 3]))  # False
# print(hasGroupsSizeX(0, [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5]))  # True
# print(hasGroupsSizeX(0, [1, 2, 3, 4, 4, 3, 2, 1]))  # True
# print(hasGroupsSizeX(0, [1, 1, 1, 2, 2, 2, 3, 3]))  # False
# print(hasGroupsSizeX(0, [1, 2]))  # False
# print(hasGroupsSizeX(0, [1, 1, 2, 2, 2, 2]))  # True
print(hasGroupsSizeX(0, [1, 1, 1, 1, 2, 2, 2, 2, 2, 2]))  # True
print(
    hasGroupsSizeX(
        0,
        [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            1,
            1,
            1,
            1,
            1,
            1,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            3,
            3,
            3,
            3,
            3,
            3,
            4,
            4,
            4,
            5,
            5,
            5,
            6,
            6,
            6,
            7,
            7,
            7,
        ],
    )
)  # True
