from collections import defaultdict, deque
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        length = len(arr)
        indices = defaultdict(list)

        for idx, num in enumerate(arr):
            indices[num].append(idx)

        queue = deque([(0, 0)])
        visited, visited_groups = set(), set()

        while queue:
            steps, idx = queue.popleft()

            if idx == length - 1:
                return steps

            # one step left, one step right of current idx
            for nxt_idx in [idx - 1, idx + 1]:
                if 0 <= nxt_idx <= length and nxt_idx not in visited:
                    visited.add(nxt_idx)
                    queue.append((steps + 1, nxt_idx))

            # check for same numbers
            if arr[idx] not in visited_groups:
                for nxt_idx in indices[arr[idx]]:
                    if nxt_idx not in visited:
                        visited.add(nxt_idx)
                        queue.append((steps + 1, nxt_idx))

                visited_groups.add(arr[idx])



obj = Solution()
print(obj.minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))
