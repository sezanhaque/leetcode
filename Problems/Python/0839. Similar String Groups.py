from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        groups = 0
        n = len(strs)
        visited = [False] * n

        for i in range(n):
            if visited[i]:
                continue
            groups += 1
            self.DFS(i, strs, visited)

        return groups

    def DFS(self, i: int, strs: List[str], visited: List[bool]) -> None:
        visited[i] = True

        for j in range(len(strs)):
            if visited[j]:
                continue
            if self.is_similar(strs[i], strs[j]):
                self.DFS(j, strs, visited)

    def is_similar(self, a: str, b: str) -> bool:
        count = 0

        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1

        return count == 2 or count == 0
