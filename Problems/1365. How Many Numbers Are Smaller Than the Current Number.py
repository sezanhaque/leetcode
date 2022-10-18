def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
    result = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                count += 1
        result.append(count)
    return result

def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
    sortedNums = sorted(nums)
    dict = {}
    result = []
    for i in range(len(sortedNums)):
        if sortedNums[i] not in dict:
            dict[sortedNums[i]] = i
    for i in range(len(nums)):
        result.append(dict[nums[i]])
    return result


def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
    sortedNums = sorted(nums)
    dict = {item: sortedNums.index(item) for item in sortedNums}
    return [dict[num] for num in nums]


print(smallerNumbersThanCurrent(0, [8, 1, 2, 2, 3]))
# print(smallerNumbersThanCurrent(0, [6, 5, 4, 8]))
# print(smallerNumbersThanCurrent(0, [7, 7, 7, 7]))
