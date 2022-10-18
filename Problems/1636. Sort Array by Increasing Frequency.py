import collections


def frequencySort(self, nums: list[int]) -> list[int]:
    count = collections.Counter(nums)
    return sorted(nums, key=lambda x: (count[x], -x))


def frequencySort(self, nums: list[int]) -> list[int]:
    return sorted(sorted(nums, reverse=True), key=nums.count)


print(frequencySort(0, [1, 1, 2, 2, 2, 3, 3, 4]))
print(frequencySort(0, [1, 5, 0, 5]))
