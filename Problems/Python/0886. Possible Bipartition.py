from collections import defaultdict, deque
from typing import List


class Solution:
    """
    This is a graph problem. It actually asks that if the graph is bipartite graph or not.

    We can divide the people into 2 groups.
    One group dislike the oder group member.

    We have to check 2 person dislike each other must not go to same group.

    Solution: (BFS)

        1.  Create a hashmap to make an adjacent list to contain
            all neighbour.

        2.  We will create a list "color" length of n
            that will assign each node a color between
            0 (red) / 1 (blue).
            Initialize it to -1 for all nodes.
            This way we will divide nodes into 2 groups.

        3.  Run a loop over all the nodes and check if there is any node i which is uncolored.

        4.  If a node has not been colored (-1), then start BFS traversal which will cover all
                *   Initialize a queue with source in the queue.
                *   Assign a color to the source, let's say 0.

        5.  Then, while the queue is not empty:
            *   Dequeue the first node from the queue.
            *   Iterate over all of its neighbour and check if any neighbour has
                same color as node. If any neighbour matches then we return False.
            *   If any color is not set yet, then assign it to the opposite color of the node.
                Then put it into the queue.

        6.  If any BFS conflicts then we return False.
            Otherwise, we return True in the end.
    """

    def __init__(self):
        self.dislike_dict = defaultdict(list)
        self.color = None

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        for a, b in dislikes:
            self.dislike_dict[a].append(b)
            self.dislike_dict[b].append(a)

        self.color = [-1] * (n + 1)

        for node in range(1, n + 1):
            if self.color[node] == -1:
                if not self.BFS(node):
                    return False
                # if not self.DFS(node, 0):
                #     return False

        return True

    # BFS Implementation
    def BFS(self, source: int) -> bool:
        queue = deque([source])
        self.color[source] = 0

        while queue:
            node = queue.popleft()

            for neighbour in self.dislike_dict[node]:
                if self.color[neighbour] == self.color[node]:
                    return False
                if self.color[neighbour] == -1:
                    self.color[neighbour] = 1 - self.color[node]
                    queue.append(neighbour)
        return True

    # DFS Implementation
    def DFS(self, node: int, color: int) -> bool:
        self.color[node] = color
        for neighbour in self.dislike_dict[node]:
            if self.color[neighbour] == self.color[node]:
                return False
            if self.color[neighbour] == -1:
                if not self.DFS(neighbour, 1 - color):
                    return False
        return True


obj = Solution()
print(obj.possibleBipartition(n=4, dislikes=[[1, 2], [1, 3], [2, 4]]))
