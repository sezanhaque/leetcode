from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        res = -1
        visited = set()

        for node in range(len(edges)):
            count, curr_node = 0, node
            cycle = {}

            while curr_node not in visited and curr_node != -1:
                count += 1

                # store current count of current node
                # to the hashmap & hashset
                visited.add(curr_node)
                cycle[curr_node] = count

                # move to the next node
                curr_node = edges[curr_node]

            # get max distance
            res = max(res, count + 1 - cycle.get(curr_node, 10 ** 5 + 1))

        return res


obj = Solution()
print(obj.longestCycle([3, 3, 4, 2, 3]))
print(obj.longestCycle([2, -1, 3, 1]))
