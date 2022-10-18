def findKthLargest(self, nums: list[int], k: int) -> int:
    return sorted(nums)[-k]


print(findKthLargest(0, [3, 2, 1, 5, 6, 4], 2))
print(findKthLargest(0, [3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
