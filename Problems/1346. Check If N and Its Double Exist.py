class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        seen = set()
        for num in arr:
            if num * 2 in seen or num / 2 in seen:
                return True
            seen.add(num)
        return False


# print(Solution.checkIfExist(0, [10, 2, 5, 3]))
print(Solution.checkIfExist(0, [3, 1, 7, 11]))
# print(Solution.checkIfExist(0, [0, 0]))
