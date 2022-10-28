from collections import Counter


def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
    count1, count2 = Counter(nums1), Counter(nums2)
    result = []

    for idx in count1:
        if idx in count2:
            if count1[idx] < count2[idx]:
                for _ in range(count1[idx]):
                    result.append(idx)
            else:
                for _ in range(count2[idx]):
                    result.append(idx)

    return result


def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
    return list((Counter(nums1) & Counter(nums2)).elements())


print(intersect(0, [1, 2, 2, 1, 5], [2, 2]))
print(intersect(0, [4, 9, 5], [9, 4, 9, 8, 4]))
