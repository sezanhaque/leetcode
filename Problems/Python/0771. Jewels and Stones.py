class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        jewels_set = set(jewels)

        for s in stones:
            if s in jewels_set:
                res += 1

        return res


obj = Solution()
print(obj.numJewelsInStones(jewels="aA", stones="aAAbbbb"))
print(obj.numJewelsInStones(jewels="z", stones="ZZ"))
