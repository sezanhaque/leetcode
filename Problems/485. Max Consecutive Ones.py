def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
    count, max_count = 0, 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
    return max_count if max_count > count else count


print(findMaxConsecutiveOnes(0, [1, 1, 0, 1, 1, 1]))
print(findMaxConsecutiveOnes(0, [1, 0, 1, 1, 0, 1]))
