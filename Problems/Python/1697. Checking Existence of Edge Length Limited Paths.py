from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        xset, yset = self.find(x), self.find(y)

        if xset != yset:
            if self.rank[xset] < self.rank[yset]:
                self.parent[xset] = yset
            else:
                self.parent[yset] = xset
            if self.rank[xset] == self.rank[yset]:
                self.rank[xset] += 1

            return True

        return False


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        union_find = UnionFind(n)

        for i, q in enumerate(queries):
            queries[i].append(i)

        queries.sort(key=lambda q: q[2])
        edgeList.sort(key=lambda e: e[2])

        i = 0
        res = [False] * len(queries)

        for q in queries:
            while i < len(edgeList) and edgeList[i][2] < q[2]:
                union_find.union(edgeList[i][0], edgeList[i][1])
                i += 1

            if union_find.find(q[0]) == union_find.find(q[1]):
                res[q[3]] = True

        return res


obj = Solution()
print(obj.distanceLimitedPathsExist(n=3, edgeList=[[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]],
                                    queries=[[0, 1, 2], [0, 2, 5]]))
