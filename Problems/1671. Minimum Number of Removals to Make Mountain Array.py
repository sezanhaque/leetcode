from itertools import count
import time


class Time_Counter:
    def __init__(self):
        self.start = time.perf_counter()

    def get_time(self):
        return time.perf_counter() - self.start

# *** Not solved ***

def minimumMountainRemovals(self, nums: list[int]) -> int:
    result = 0
    mountainPoint = nums.index(max(nums))
    result = result + twoPointers(0, nums[0 : mountainPoint + 1], True)
    # result = result + twoPointers(0, nums[mountainPoint + 1 :], False)
    return result


# def twoPointers(self, nums: list[int], isAscOrder: True) -> int:
#     left, right, counter = 0, 1, 0

#     while right < len(nums):
#         if isAscOrder:
#             if nums[left] >= nums[right]:
#                 nums.remove(nums[left])
#                 counter += 1
#             else:
#                 left += 1
#                 right += 1
#         else:
#             if nums[left] <= nums[right]:
#                 nums.remove(nums[right])
#                 counter += 1
#             else:
#                 left += 1
#                 right += 1
#     print(nums)
#     return counter


def twoPointers(self, nums: list[int], isAscOrder: True) -> int:
    counter = 0

    if isAscOrder:
        right = len(nums) - 2
        left = right - 1
        lowest = nums[right]
        while left > -1:
            lowest = min(lowest, nums[left])
            if nums[right] > lowest:
                del nums[right]
                counter += 1
            elif nums[left] >= nums[right]:
                # nums.remove(nums[left])
                del nums[right]
                counter += 1
            else:
                left -= 1
                right -= 1
    else:
        left, right = 0, 1
        lowest = nums[left]
        while right < len(nums):
            lowest = min(lowest, nums[right])
            if nums[left] < lowest:
                del nums[left]
                counter += 1
            elif nums[left] <= nums[right]:
                # nums.remove(nums[right])
                del nums[right]
                counter += 1
            else:
                left += 1
                right += 1

    # while right < len(nums):
    #     if isAscOrder:
    #         if nums[left] >= nums[right]:
    #             nums.remove(nums[left])
    #             counter += 1
    #         else:
    #             left += 1
    #             right += 1
    #     else:
    #         if nums[left] <= nums[right]:
    #             nums.remove(nums[left])
    #             counter += 1
    #         else:
    #             left += 1
    #             right += 1
    print(nums)
    return counter


def minimumMountainRemovals(self, nums: list[int]) -> int:
    n = len(nums)
    inc = [0] * n
    dec = [0] * n

    #  Longest Increasing Subsequence
    for i in range(1, n):
        for j in range(0, i):
            if nums[i] > nums[j]:
                inc[i] = max(inc[i], inc[j] + 1)

    #  Longest Decreasing Subsequence
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if nums[i] > nums[j]:
                dec[i] = max(dec[i], dec[j] + 1)

    print(inc, dec)


counter = Time_Counter()

# print(minimumMountainRemovals(0, [3, 2, 1, 1, 5, 6, 2, 3, 1]))  # 4

# try for left double value, expected 2 but 3
# print(minimumMountainRemovals(0, [2, 1, 2, 1, 3, 5, 6, 3, 2, 1]))

# expected 6 but 5
# print(minimumMountainRemovals(0, [2, 1, 1, 5, 6, 2, 2, 3, 1, 4, 3]))

# try for left, expected 3 but 4
# print(minimumMountainRemovals(0, [2, 1, 2, 1, 5, 4, 6, 3, 2, 1]))

print(minimumMountainRemovals(0, [2, 1, 1, 5, 6, 2, 3, 1]))  # 3
# print(minimumMountainRemovals(0, [1, 3, 1]))

# expected 4 but 3
# print(minimumMountainRemovals(0, [4, 3, 2, 1, 1, 2, 3, 1]))

print(counter.get_time())
