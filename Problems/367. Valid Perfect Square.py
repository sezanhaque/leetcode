def isPerfectSquare(self, num: int) -> bool:
    """
    Faster
    """
    result = num

    while result * result > num:
        result = (result + num // result) >> 1

    return result * result == num


def isPerfectSquare(self, num: int) -> bool:
    """
    Bit Manipulation
    """
    root = 0
    bit = 1 << 15

    while bit > 0:
        root |= bit
        if root > num // root:
            root ^= bit
        bit >>= 1
    return root * root == num


def isPerfectSquare(self, num: int) -> bool:
    """
    Binary Search
    """
    left = 0
    right = num

    while left <= right:
        mid = left + ((right - left) >> 1)
        if mid**2 == num:
            return True
        elif mid**2 > num:
            right = mid - 1
        else:
            left = mid + 1
    return False


# print(isPerfectSquare(0, 16))
# print(isPerfectSquare(0, 14))
# print(isPerfectSquare(0, 1))
print(isPerfectSquare(0, 8))
print(isPerfectSquare(0, 144))
