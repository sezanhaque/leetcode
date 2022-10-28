def sortedSquares(self, nums: list[int]) -> list[int]:
    """
    Using built in sort function
    """
    for i in range(len(nums)):
        nums[i] *= nums[i]
    nums.sort()
    return nums

    # return sorted(map(lambda x: x * x, nums))
    # return sorted([i**2 for i in nums])


def sortedSquares(self, nums: list[int]) -> list[int]:
    """
    Two Pointers method
    """

    result = [None] * len(nums)
    left, right = 0, len(nums) - 1
    for index in range(len(nums) - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[index] = nums[left] ** 2
            left += 1
        else:
            result[index] = nums[right] ** 2
            right -= 1
    return result


print(sortedSquares(0, [-4, -1, 0, 3, 10]))
print(sortedSquares(0, [-7, -3, 2, 3, 11]))
