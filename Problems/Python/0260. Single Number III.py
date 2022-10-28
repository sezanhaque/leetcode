def singleNumber(self, nums: list[int]) -> int:
    dict = {}
    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return [key for key, value in dict.items() if value == 1]


print(singleNumber(0, [1, 2, 1, 3, 2, 5]))
