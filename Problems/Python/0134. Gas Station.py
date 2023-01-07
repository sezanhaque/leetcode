from typing import List


class Solution:
    """
    If total gas is less than total cost then we won't able to get the result.
    So return -1.

    If not then there must be an ans.

    So we are traversing from first to last to check where the total gas is less than 0.
    If it is less than 0 then we assume the result will be next idx.
    So we go to the next idx and make total gas 0.

    Lastly return res.
    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        res = total_gas = 0

        for idx in range(len(gas)):
            total_gas += gas[idx] - cost[idx]
            if total_gas < 0:
                res = idx + 1
                total_gas = 0

        return res


obj = Solution()
print(obj.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
