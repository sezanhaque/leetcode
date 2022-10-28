def mySqrt(self, x: int) -> int:
    return int(x**0.5)


def mySqrt(self, x: int) -> int:
    """
    Binary Search
    """
    if x == 1:
        return 1  # deal with exception
    left, right = 0, x

    while left <= right:
        mid = (right + left) // 2
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif x < mid * mid:
            right = mid
        else:
            left = mid


def mySqrt(self, x: int) -> int:
    result = x
    while result * result > x:
        result = (result + x // result) >> 1
    return result


print(mySqrt(0, 8))
