def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
    dic = {}
    for idx, num in enumerate(nums):
        if num in dic and idx - dic[num] <= k:
            return True
        dic[num] = idx
    return False


# print(containsNearbyDuplicate(0, [1, 2, 3, 1], 3))
print(containsNearbyDuplicate(0, [1, 2, 3, 1, 2, 3], 2))
