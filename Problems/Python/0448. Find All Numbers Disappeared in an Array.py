def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
    new_set = set(nums)
    result = []
    for i in range(1, len(nums) + 1):
        if i not in new_set:
            result.append(i)
    return result


print(findDisappearedNumbers(0, [4, 3, 2, 7, 8, 2, 3, 1]))
