from collections import Counter
from itertools import chain, product
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_len, col_len, word_len = len(board), len(board[0]), len(word)

        # there are not enough letters in the board
        if word_len > row_len * col_len:
            return False

        # there are not enough letters in the board
        if not (cnt := Counter(word)) <= Counter(chain(*board)):
            return False

        # if it is better to start from end
        if cnt[word[0]] > cnt[word[-1]]:
            word = word[::-1]

        def DFS(row_idx: int, col_idx: int, word_idx: int) -> bool:
            if word_idx == word_len:
                return True

            # if row_idx, col_idx are in range
            # and current char from word is as same as board char
            if 0 <= row_idx < row_len and \
                    0 <= col_idx < col_len and \
                    board[row_idx][col_idx] == word[word_idx]:

                # make the idx as seen
                board[row_idx][col_idx] = '#'

                # -> bottom, -> right, -> top, -> left
                path = [(row_idx + 1, col_idx), (row_idx, col_idx + 1), (row_idx - 1, col_idx), (row_idx, col_idx - 1)]

                res = any(DFS(row, col, word_idx + 1) for row, col in path)

                # undo the change
                board[row_idx][col_idx] = word[word_idx]

                return res

            return False

        return any(DFS(i, j, 0) for i, j in product(range(row_len), range(col_len)))


obj = Solution()
print(obj.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED"))
