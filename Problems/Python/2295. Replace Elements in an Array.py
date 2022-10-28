def arrayChange(self, nums: list[int], operations: list[list[int]]) -> list[int]:
    """
    Time Limit Exceeded
    """
    for operation in operations:
        nums[nums.index(operation[0])] = operation[1]
    return nums


def arrayChange(self, nums: list[int], operations: list[list[int]]) -> list[int]:
    my_dict = {num: i for i, num in enumerate(nums)}

    for prev, new_val in operations:
        nums[my_dict[prev]] = new_val
        my_dict[new_val] = my_dict[prev]
        del my_dict[prev]
    return nums


print(arrayChange(0, [1, 2, 4, 6], [[1, 3], [4, 7], [6, 1]]))
# print(arrayChange(0, [1, 2], [[1, 3], [2, 1], [3, 2]]))
