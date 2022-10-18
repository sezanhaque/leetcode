def missingNumber(self, nums: list[int]) -> int:
    """Slowest solution"""
    missing_number = 0
    for i in range(0, len(nums) + 1):
        if i not in nums:
            missing_number = i
    return missing_number


def missingNumber(self, nums: list[int]) -> int:
    """Using SUM function, Fast"""
    return sum(range(len(nums) + 1)) - sum(nums)


"""
Sum of the First n Terms of a Series
Sn=n(a1 + a2)//2
"""


def missingNumber(self, nums: list[int]) -> int:
    """Fast solution"""
    n = len(nums)
    return ((n * (n + 1)) // 2) - sum(nums)


print(missingNumber(0, [3, 0, 1]))
print(missingNumber(0, [0, 1]))
print(missingNumber(0, [9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(missingNumber(0, [1]))
