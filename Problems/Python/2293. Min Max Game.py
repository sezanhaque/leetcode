def minMaxGame(self, nums: list[int]) -> int:
    length = len(nums)
    if length == 1:
        return nums[0]

    while length > 0:
        i = 1
        count = 0
        while i <= length:
            if count % 2 == 0:
                nums[count] = min(nums[i], nums[i - 1])
            else:
                nums[count] = max(nums[i], nums[i - 1])
            count += 1
            i += 2
        length = length // 2
    return nums[0]


# print(minMaxGame(0, [1, 3, 5, 2, 4, 8, 2, 2]))
print(minMaxGame(0, [70, 38, 21, 22]))
