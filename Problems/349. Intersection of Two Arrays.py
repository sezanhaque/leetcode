def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
    result = []

    for i in nums1:
        if i in nums2 and i not in result:
            result.append(i)
    return result


def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
    nums1, nums2 = set(nums1), set(nums2)

    if len(nums1) < len(nums2):
        return [n for n in nums1 if n in nums2]
    else:
        return [n for n in nums2 if n in nums1]


def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
    return set(nums1) & (set(nums2))


print(intersection(0, [1, 2, 2, 1], [2, 2]))
print(intersection(0, [4, 9, 5], [9, 4, 9, 8, 4]))
