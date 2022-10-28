from itertools import count


def countElements(self, nums: list[int]) -> int:
    """
    Fast
    """
    nums = sorted(nums)
    smallest = nums[0]
    largest = nums[-1]

    if smallest == largest:
        return 0

    small_count = nums.count(smallest)
    large_count = nums.count(largest)
    return len(nums) - small_count - large_count

def countElements(self, nums: list[int]) -> int:
    smallest = min(nums)
    largest = max(nums)

    return sum(1 for i in nums if smallest < i < largest)


print(countElements(0, [11, 7, 2, 15]))
print(countElements(0, [-3, 3, 3, 90]))
print(countElements(0, [0]))
