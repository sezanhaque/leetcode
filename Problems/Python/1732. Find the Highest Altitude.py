from itertools import accumulate


def largestAltitude(self, gain: list[int]) -> int:
    return max([0] + list(accumulate(gain)))

def largestAltitude(self, gain: list[int]) -> int:
    return max(accumulate(gain, initial=0))


print(largestAltitude(0, [-5, 1, 5, 0, -7]))
print(largestAltitude(0, [-4, -3, -2, -1, 4, 3, 2]))
