class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        result = []
        minimum = float("inf")

        for i in range(len(arr) - 1):
            current = arr[i + 1] - arr[i]
            if current < minimum:
                minimum = current

        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == minimum:
                result.append([arr[i], arr[i + 1]])

        return result

    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        minimum = min(b - a for a, b in zip(arr, arr[1:]))
        return [[a, b] for a, b in zip(arr, arr[1:]) if b - a == minimum]


print(Solution.minimumAbsDifference(0, [4, 2, 1, 3]))
