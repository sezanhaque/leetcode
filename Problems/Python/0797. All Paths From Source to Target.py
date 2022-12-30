from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res: List[List[int]] = []
        tmpArr: List[int] = []

        def DFS(idx: int):
            tmpArr.append(idx)

            if idx == len(graph) - 1:
                res.append(list(tmpArr))
            else:
                for i in graph[idx]:
                    DFS(i)

            tmpArr.pop()

        DFS(0)
        return res

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res: List[List[int]] = []

        def DFS(curr_idx: int, path: List[int]):
            if curr_idx == len(graph) - 1:
                res.append(path)
            else:
                for i in graph[curr_idx]:
                    DFS(i, path + [i])

        DFS(0, [0])
        return res


obj = Solution()
print(obj.allPathsSourceTarget([[1, 2], [3], [3], []]))
