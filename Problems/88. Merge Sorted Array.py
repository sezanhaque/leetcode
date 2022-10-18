def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    From the index of m in nums1, insert nums2 from index 0 to n
    """
    nums1[m:] = nums2[:n]
    nums1.sort()
    print(nums1)


merge(0, [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
merge(0, [1], 1, [], 0)
merge(0, [0], 0, [1], 1)
