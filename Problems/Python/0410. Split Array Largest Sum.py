def splitArray(self, nums: list[int], m: int) -> int:
    left, right = max(nums), sum(nums)

    while left < right:

        mid = left + ((right - left) >> 1)
        totalSum, currentSubArray = 0, 1

        for num in nums:
            if totalSum + num <= mid:
                totalSum += num
            else:
                totalSum = num
                currentSubArray += 1

        # If current Sub array count is greater than m, then it means we made more subarrays than m
        # So we need to compress the limit to mid + 1
        # Otherwise right = mid
        if currentSubArray > m:
            left = mid + 1
        else:
            right = mid

    return right


print(splitArray(0, [7, 2, 5, 10, 8], 2))
# print(splitArray(0, [10, 20, 30, 40], 2))
# print(splitArray(0, [1, 2, 3, 4, 5], 2))
# print(splitArray(0, [1, 4, 4], 3))
# print(splitArray(0, [2, 16, 14, 15], 2))  # expected 29 but 31
