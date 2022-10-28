from math import inf


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False

        first, second = inf, inf
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False


if __name__ == "__main__":
    # print(Solution.increasingTriplet(0, [1, 2, 3, 4, 5]))
    # print(Solution.increasingTriplet(0, [5, 4, 3, 2, 1]))
    # print(Solution.increasingTriplet(0, [2, 1, 5, 0, 4, 6]))
    print(Solution.increasingTriplet(0, [20, 100, 10, 12, 5, 13, 14]))
