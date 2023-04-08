class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hashmap = {}

        def DFS(node: Node) -> Node:
            if node in hashmap:
                return hashmap[node]

            copy = Node(node.val)
            hashmap[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(DFS(neighbor))

            return copy

        return DFS(node) if node else None
