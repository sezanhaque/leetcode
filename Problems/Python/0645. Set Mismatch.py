def findErrorNums(self, nums: list[int]) -> list[int]:
    new_arr = [x for x in range(1, len(nums) + 1)]
    nums = sorted(nums)
    duplicate_number, missing_number = 0, 0
    left, right = 0, 1

    # duplicate number
    while right < len(nums):
        if nums[left] != right and missing_number is None:
            missing_number = right

        if nums[left] == nums[right]:
            duplicate_number = nums[left]
            left += 1
            right += 1
        else:
            left += 1
            right += 1
    return [duplicate_number, abs(sum(nums) - sum(new_arr) - duplicate_number)]


def findErrorNums(self, nums: list[int]) -> list[int]:
    # Create a unique and sorted list of all numbers
    unique_numbers = set(nums)

    # Create a list of all numbers from 1 to n
    one_to_n = [x for x in range(1, len(nums) + 1)]

    # Find the duplicate number
    duplicate_number = sum(nums) - sum(unique_numbers)
    return [duplicate_number, abs(sum(nums) - sum(one_to_n) - duplicate_number)]


print(findErrorNums(0, [1, 2, 2, 4]))
print(findErrorNums(0, [1, 1]))
print(findErrorNums(0, [3, 2, 2]))  # [2,1]
print(findErrorNums(0, [3, 2, 3, 4, 6, 5]))  # [3,1]
print(findErrorNums(0, [1, 5, 3, 2, 2, 7, 6, 4, 8, 9]))  # [2,10]
