class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        res = partition = 0

        for num in s:
            # if current partition * 10 + num > k
            # then we have 1 res so res += 1
            # now we will check next num so
            # partition = 0
            if partition * 10 + int(num) > k:
                res += 1
                partition = 0

            partition = partition * 10 + int(num)

            if partition > k:
                return -1

        return res + 1


obj = Solution()
print(obj.minimumPartition(s="165462", k=60))
print(obj.minimumPartition(s="238182", k=5))
