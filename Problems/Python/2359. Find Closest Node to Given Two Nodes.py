from math import inf
from typing import List


class Solution:
    """
    Approach:

    1.  Initialize variables n to the size of the edges array, res to -1, and minDist to the maximum value of an int.

    2.  Create two arrays dist1 and dist2 of size n and initialize all elements to 0.
        Also, create two arrays visited1 and visited2 of size n and initialize all elements to false.

    3.  Run the depth-first search (DFS) algorithm from node1 and update the dist1 and visited1 arrays accordingly.

    4.  Run the DFS algorithm from node2 and update the dist2 and visited2 arrays accordingly.

    5.  Iterate through all nodes currNode in the graph.

    6.  For each node, check if it has been visited by both DFS calls, and if its maximum distance from node1 and node2
        (i.e. max(dist1[currNode], dist2[currNode])) is less than the current value of minDist.

    7.  If the above conditions are met, update the value of minDist and res to the current node's distance and index,
        respectively.

    8.  Return res as the result.

    This algorithm finds the closest meeting point between two given nodes in a graph by using DFS to calculate the
    distance from each node to all other nodes in the graph. It only considers nodes that are reachable from both given
    nodes, and chooses the one that has the smallest maximum distance from the two given nodes.

    Complexity:
        Time complexity: O(n) // where n is the number of nodes
        Space complexity: O(n) // we are using visited, distance array of size n
    """
    def DFS(self, node: int, visited: List[bool], distance: List[int], edges: List[int]):
        # make the current node as visited
        visited[node] = True

        # get the neighbor of current node
        neighbor = edges[node]

        # if neighbour has edges and neighbor is not visited
        if neighbor != -1 and not visited[neighbor]:
            # add the distance of neighbor with current node + 1
            distance[neighbor] = distance[node] + 1

            # now DFS current neighbor
            self.DFS(neighbor, visited, distance, edges)

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        length = len(edges)
        res, minDist = -1, inf

        # store distance of node1 and node2 from all others nodes
        dist1, dist2 = [0] * length, [0] * length

        # store visited nodes for DFS
        visited1, visited2 = [False] * length, [False] * length

        self.DFS(node1, visited1, dist1, edges)
        self.DFS(node2, visited2, dist2, edges)

        for currNode in range(length):
            # if current node is visited in both visited and
            # minDist is greater than max of dist1 and dist2
            # then update maxDist
            if (
                    visited1[currNode] and visited2[currNode]
                    and minDist > max(dist1[currNode], dist2[currNode])
            ):
                minDist = max(dist1[currNode], dist2[currNode])
                res = currNode

        return res


obj = Solution()
print(obj.closestMeetingNode(edges=[2, 2, 3, -1], node1=0, node2=1))  # 2
