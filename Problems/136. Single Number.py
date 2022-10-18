def singleNumber(self, nums: list[int]) -> int:
    dict = {}
    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return min(dict, key=dict.get)


print(singleNumber(0, [2, 2, 1]))
print(singleNumber(0, [4, 1, 2, 1, 2]))
print(singleNumber(0, [1]))
