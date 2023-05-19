from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        return list(set(range(n)) - set(j for i, j in edges))


obj = Solution()
print(obj.findSmallestSetOfVertices())