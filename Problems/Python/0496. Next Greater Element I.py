from collections import deque


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack, nextGreater = deque(), dict.fromkeys(nums2, -1)
        for val in nums2:
            while stack and stack[-1] < val:
                nextGreater[stack.pop()] = val
            stack.append(val)

        return [nextGreater[val] for val in nums1]

        # or as a generator (faster than list)
        # return (nextGreater[val] for val in nums1)

        # or using map
        # return map(nextGreater.get, nums1)

    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        for n in nums1:
            res.append(next((m for m in nums2[nums2.index(n) :] if m > n), -1))
        return res

    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # 1 liner
        return (next((m for m in nums2[nums2.index(n) :] if m > n), -1) for n in nums1)

print(Solution.nextGreaterElement(0, nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))  # [-1, 3, 1]
