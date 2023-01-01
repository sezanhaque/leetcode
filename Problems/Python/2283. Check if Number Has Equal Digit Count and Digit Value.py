from collections import Counter


class Solution:
    def digitCount(self, num: str) -> bool:
        counts = Counter(map(int, num))

        for idx, val in enumerate(num):
            if counts[idx] != int(val):
                return False

        return True

    def digitCount(self, num: str) -> bool:
        counts = Counter(map(int, num))
        return all(counts[idx] == int(val) for idx, val in enumerate(num))


obj = Solution()
print(obj.digitCount("1210"))
