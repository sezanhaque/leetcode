def hammingWeight(self, n) -> int:
    """
    This result is correct for Leet code problem
    """
    return str(bin(int(n)))[2:].count('1')


def hammingWeight(self, n: int) -> int:
    num_of_1s = 0

    for _ in range(32):
        num_of_1s += n & 1
        n = n >> 1

    return num_of_1s


print(hammingWeight(0, "00000000000000000000000000001011"))
