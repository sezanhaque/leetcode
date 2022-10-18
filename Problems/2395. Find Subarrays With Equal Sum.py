def findSubarrays(self, nums: list[int]) -> bool:
    count = 1
    sums = []
    my_sum = 0

    for i in range(len(nums) - 1):
        my_sum = nums[i] + nums[i + 1]
        if my_sum not in sums:
            sums.append(my_sum)
        else:
            count += 1
        if count == 2:
            return True
    return False


def findSubarrays(self, nums: list[int]) -> bool:
    sums = set()

    for i in range(len(nums) - 1):
        getSum = nums[i] + nums[i + 1]
        if getSum in sums:
            return True
        sums.add(getSum)
    return False


print(findSubarrays(0, [4, 2, 4]))
print(findSubarrays(0, [1, 2, 3, 4, 5]))
print(findSubarrays(0, [0, 0, 0]))
print(findSubarrays(0, [0, 0]))
print(findSubarrays(0, [1, 2, 3, 2, 1]))
print(
    findSubarrays(
        0,
        [
            77,
            95,
            90,
            98,
            8,
            100,
            88,
            96,
            6,
            40,
            86,
            56,
            98,
            96,
            40,
            52,
            30,
            33,
            97,
            72,
            54,
            15,
            33,
            77,
            78,
            8,
            21,
            47,
            99,
            48,
        ],
    )
)
