from collections import defaultdict


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        adj = defaultdict(set)

        for a, b in zip(s1, s2):
            adj[a].add(b)
            adj[b].add(a)

        def DFS(char: str, minChar: str, visited: set) -> str:
            visited.add(char)
            res = minChar

            for child in adj[char]:
                if child not in visited:
                    res = min(res, DFS(child, min(child, minChar), visited))

            return res

        return "".join(DFS(c, c, set()) for c in baseStr)


obj = Solution()
print(obj.smallestEquivalentString(s1="parker", s2="morris", baseStr="parser"))
