def shuffle(self, nums: list[int], n: int) -> list[int]:
    """
    Fast
    """
    result = []
    for i in range(0, n):
        result.append(nums[i])
        result.append(nums[i + n])
    return result


def shuffle(self, nums: list[int], n: int) -> list[int]:
    return [num for idx in zip(nums[:n], nums[n:]) for num in idx]


print(shuffle(0, [2, 5, 1, 3, 4, 7], 3))
print(shuffle(0, [1, 2, 3, 4, 4, 3, 2, 1], 4))
