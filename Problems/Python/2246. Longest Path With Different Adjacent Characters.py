from collections import defaultdict
from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        res = 1
        adj = defaultdict(list[int])

        # make adjacent list from parent list
        for i in range(1, len(parent)):
            adj[parent[i]].append(i)
            adj[i].append(parent[i])

        def DFS(currNode: int, parent: int) -> int:
            nonlocal res

            longestChain = secondLongestChain = 0

            for child in adj[currNode]:
                if child == parent:
                    continue

                # Get the number of nodes from child
                longestChainFromChild = DFS(child, currNode)

                # if currNode node and child are same
                # then skip them
                if s[child] == s[currNode]:
                    continue

                # modify the longestChain and secondLongestChain
                # if longestChainFromChild is bigger
                if longestChainFromChild > longestChain:
                    longestChain, secondLongestChain = longestChainFromChild, longestChain
                elif longestChainFromChild > secondLongestChain:
                    secondLongestChain = longestChainFromChild

            # checking max value between res and current rounded subtree
            # and store it to res
            res = max(res, longestChain + secondLongestChain + 1)

            # But we are returning the longest path between the rounded subtree
            # Because in tree we can not generate tree branches for the current node path
            return longestChain + 1

        DFS(0, -1)
        return res


obj = Solution()
print(obj.longestPath(parent=[-1, 0, 0, 1, 1, 2], s="abacbe"))
