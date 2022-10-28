def reverseBits(self, n: int) -> int:
    """
    Bitwise operation
    Make the binary number to 32 bit with zfill(32)
    then iterate from back to front
    then make it int
    """
    return int(bin(n)[2:].zfill(32)[::-1], 2)


def reverseBits(self, n: int) -> int:
    res = 0
    for _ in range(32):
        res = (res << 1) + (n & 1)
        n >>= 1
    return res


def reverseBits(self, n: int) -> int:
    """
    The '032b' says to give back the integer as binary string, with 32 bits, and initial zeros to fill in the 32 bits.
    Then, we reverse the string.
    Then, we convert the string back to integer.
    """
    bit_str = "{0:032b}".format(n)
    reverse_str = bit_str[::-1]
    return int(reverse_str, 2)


print(reverseBits(0, 0b000010100101000001111010011100))
