from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)

        visited = set()
        queue = deque()
        queue.append((1, 0))

        def label_to_position(label: int) -> tuple[int, int]:
            row, col = divmod(label - 1, length)

            # if row is even
            if not row & 1:
                return length - 1 - row, col
            else:
                return length - 1 - row, length - 1 - col

        while queue:
            label, step = queue.popleft()
            row, col = label_to_position(label)

            # if current block is not -1, it means
            # it will be a snack or ladder, so
            # change the label to it
            if board[row][col] != -1:
                label = board[row][col]

            # if label is equal to n^2
            # then we have reached the square
            if label == length * length:
                return step

            # iterate from 1 to 6 block
            for idx in range(1, 7):
                new_label = label + idx
                if new_label <= length * length and new_label not in visited:
                    visited.add(new_label)
                    queue.append((new_label, step + 1))

        return -1

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        need = {1: 0}
        bfs = [1]

        for dice in bfs:
            for label in range(dice + 1, dice + 7):
                row, col = divmod(label - 1, length)
                next_label = board[~row][col if not row & 1 else ~col]

                if next_label > 0:
                    label = next_label

                if label == length * length:
                    return need[dice] + 1

                if label not in need:
                    need[label] = need[dice] + 1
                    bfs.append(label)
        return -1


obj = Solution()
print(obj.snakesAndLadders(
    [[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1],
     [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]))  # 4
