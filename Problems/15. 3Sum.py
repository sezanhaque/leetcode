def threeSum(self, nums: list[int]) -> list[list[int]]:
    nums.sort()
    result, seen = [], set()
    for idx in range(len(nums) - 1):
        if nums[idx] not in seen:
            left, right = idx + 1, len(nums) - 1
            while left < right:
                remaining = nums[idx] + nums[left] + nums[right]
                if remaining == 0:
                    ans = [nums[idx], nums[left], nums[right]]
                    if ans not in result:
                        result.append(ans)
                    left += 1
                    right -= 1
                elif remaining < 0:
                    left += 1
                elif remaining > 0:
                    right -= 1
        seen.add(nums[idx])
    return result


def threeSum(self, nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    for idx in range(len(nums) - 2):
        # renamed this to idx because this will always be the leftmost pointer in the triplet
        if idx > 0 and nums[idx] == nums[idx - 1]:
            # this step makes sure that we do not have any duplicates in our result output
            continue
        left = idx + 1
        # renamed this to left because this is the pointer that is between the idx and right pointers
        right = len(nums) - 1
        while left < right:
            currSum = nums[idx] + nums[left] + nums[right]
            if currSum < 0:
                left += 1
            elif currSum > 0:
                right -= 1
            else:
                result.append([nums[idx], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    # Another conditional for not calculating duplicates
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    # Avoiding duplicates check
                    right -= 1
                left += 1
                right -= 1
    return result


print(threeSum(0, [-1, 0, 1, 2, -1, -4]))
print(threeSum(0, [0, 1, 1]))
print(threeSum(0, [-2, 0, 0, 2, 2]))  # [[-2,0,2]]
print(threeSum(0, [0, 0, 0]))
print(threeSum(0, [1, -1, -1, 0]))
print(threeSum(0, [-2, 0, 1, 1, 2]))
print(threeSum(0, [3, -2, 1, 0]))  # [[]]
print(threeSum(0, [1, -1, 0]))  # [[-1,0,1]]
print(threeSum(0, [1, 0, -1, 0, -2, 2]))  # [[-2,0,2],[-1,0,1]]
