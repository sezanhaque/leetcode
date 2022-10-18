from collections import Counter
def divideArray(self, nums: list[int]) -> bool:
    my_set = set()
    for i in range(len(nums)):
        if nums[i] not in my_set:
            count = nums.count(nums[i])
            if count % 2 != 0:
                return False
        my_set.add(nums[i])

    return True

def divideArray(self, nums: list[int]) -> bool:
    return all(i % 2 == 0 for i in Counter(nums).values())


print(divideArray(0, [1, 2, 3, 4]))
print(divideArray(0, [3, 2, 3, 2, 2, 2]))
