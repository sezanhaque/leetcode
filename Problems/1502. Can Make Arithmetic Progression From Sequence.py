class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        difference = abs(arr[0] - arr[1])
        return all(
            difference == abs(arr[i] - arr[i + 1]) for i in range(1, len(arr) - 1)
        )

    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        difference = arr[0] - arr[1]
        for i in range(1, len(arr) - 1):
            if arr[i] - arr[i + 1] != difference:
                return False
        return True


# print(Solution.canMakeArithmeticProgression(0, [3, 5, 1]))
print(Solution.canMakeArithmeticProgression(0, [1, 2, 4, 5, 8]))
# print(Solution.canMakeArithmeticProgression(0, [3, 5]))
