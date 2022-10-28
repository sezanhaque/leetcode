import collections


def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    counts = collections.Counter(nums)
    return [key for key, value in counts.most_common(k)]


print(topKFrequent(0, [1, 1, 1, 2, 2, 3], 2))
print(topKFrequent(0, [1], 1))
print(topKFrequent(0, [1, 2], 2))
print(topKFrequent(0, [3, 0, 1, 0], 1))
