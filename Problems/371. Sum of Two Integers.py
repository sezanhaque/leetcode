# def getSum(self, a: int, b: int) -> int:
#     return sum([a, b])


def getSum(self, a: int, b: int) -> int:
    """
    Bit Manipulation
    """
    # 32 bits integer max
    MAX = 0x7FFFFFFF
    # 32 bits interger min
    MIN = 0x80000000
    # mask to get last 32 bits
    mask = 0xFFFFFFFF
    while b != 0:
        # ^ get different bits and & gets double 1s, << moves carry
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask
    # if a is negative, get a's 32 bits complement positive first
    # then get 32-bit positive's Python complement negative
    return a if a <= MAX else ~(a ^ mask)


def getSum(self, a: int, b: int) -> int:
    """
    :type a: int
    :type b: int
    :rtype: int
    Bit Manipulation
    """
    mask = 0xFFFFFFFF
    while b:
        sum = (a ^ b) & mask
        carry = ((a & b) << 1) & mask
        a = sum
        b = carry

    # Warning: this return statement is not correct yet!!!
    return a


print(getSum(0, 0, -1))
