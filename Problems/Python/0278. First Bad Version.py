def firstBadVersion(self, n: int) -> int:
    """
    Two pointers solution
    """
    left, right = 0, n
    while left <= right:
        # mid = left + (right - left) // 2
        mid = (left + right) // 2
        if isBadVersion(mid):
            if not isBadVersion(mid - 1):
                return mid
            else:
                right = mid - 1
        else:
            left = mid + 1
    return left


def isBadVersion(version: int) -> bool:
    if version == 2:
        return True
    elif version == 4:
        return True
    elif version == 1702766719:
        return True
    return False


# print(firstBadVersion(0, 5))
# print(firstBadVersion(0, 2))
print(firstBadVersion(0, 2126753390))
