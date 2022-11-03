from collections import Counter, defaultdict
from sortedcontainers import SortedList

class Solution:
    def destroyTargets(self, nums: list[int], space: int) -> int:
        seeding = defaultdict(list)

        # for i in nums:
        #     seeding[i % space].append(i)
        #               Or

        [seeding[i % space].append(i) for i in nums]

        return sorted((-len(value), min(value)) for value in seeding.values())[0][1]

    def destroyTargets(self, nums: list[int], space: int) -> int:
        """
        The elements with same remainder module by space,
        can be destroyed together.
        """
        count = Counter(num % space for num in nums)
        maxValues = max(count.values())
        return min(num for num in nums if count[num % space] == maxValues)


print(Solution.destroyTargets(0, [3, 7, 8, 1, 1, 5], 2))
# print(Solution.destroyTargets(0, nums=[1, 3, 5, 2, 4, 6], space=2))
# print(Solution.destroyTargets(0, nums=[6, 2, 5], space=100))
