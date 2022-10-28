def findDuplicates(self, nums: list[int]) -> list[int]:
    """
    Time limit exceeds
    """
    result = []
    new_set = set()
    for i in range(len(nums)):
        if nums[i] not in new_set:
            result.append(nums[i]) if nums.count(nums[i]) == 2 else None
        new_set.add(nums[i])
    return result


def findDuplicates(self, nums: list[int]) -> list[int]:
    result, my_dict = [], {}

    for i in range(len(nums)):
        if nums[i] in my_dict:
            my_dict[nums[i]] += 1
        else:
            my_dict[nums[i]] = 1

    for key, value in my_dict.items():
        result.append(key) if value == 2 else None

    return result


def findDuplicates(self, nums: list[int]) -> list[int]:
    duplicate, result = set(), []

    for num in nums:
        result.append(num) if num in duplicate else duplicate.add(num)
        
    return result


print(findDuplicates(0, [4, 3, 2, 7, 8, 2, 3, 1]))
