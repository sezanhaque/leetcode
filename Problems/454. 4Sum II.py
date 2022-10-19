from collections import Counter, defaultdict


class Solution:
    def fourSumCount(
        self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]
    ) -> int:
        """
        Using Hashmap

        A + B + C + D = 0
        So, A + B = 0 - (C + D)
        """
        dict = defaultdict(int)
        count = 0

        for i in nums1:
            for j in nums2:
                dict[i + j] += 1

        for k in nums3:
            for l in nums4:
                count += dict[0 - (k + l)]
        return count

    def fourSumCount(
        self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]
    ) -> int:
        """
        Using counter method
        """
        ab = Counter(a + b for a in nums1 for b in nums2)
        return sum(ab[-c - d] for c in nums3 for d in nums4)


print(Solution.fourSumCount(0, [1, 2], [-2, -1], [-1, 2], [0, 2]))
print(Solution.fourSumCount(0, [0], [0], [0], [0]))
print(Solution.fourSumCount(0, [-1, -1], [-1, 1], [-1, 1], [1, -1]))
