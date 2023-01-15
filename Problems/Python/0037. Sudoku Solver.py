from collections import defaultdict
from itertools import product
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)
        to_visit = []  # track empty blocks
        nums = [str(n) for n in range(1, 10)]

        # iterate through board to track empty cells
        # and add them to "to_visit"
        # otherwise add the row value to rows
        # col value to cols and 3x3 boxes
        for r, c in product(range(9), range(9)):
            # checking val = board[r][c]), which is == "." or not
            # if true then it is empty so add it to to_visit
            if (val := board[r][c]) == ".":
                to_visit.append((r, c))

            # else we are adding it to rows, cols and boxes
            else:
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3, c // 3)].add(val)

        def backtrack():
            # if we don't have any block to visit
            # then the sudoku is solved, return True
            if not to_visit:
                return True

            row, col = to_visit.pop()
            box = (row // 3, col // 3)

            # iterate from "1-9"
            for num in nums:
                # check if the num is in current row, col or box
                if num not in rows[row] and num not in cols[col] and num not in boxes[box]:
                    # if not then we are changing the current block of the board to num to
                    # check if it is okay and add the num to rows, cols and boxes to track
                    board[row][col] = num
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box].add(num)

                    # again backtracking to check if every condition is okay for this num
                    if backtrack():
                        return True

                    # after backtracking, we are reverting the changes we had made before
                    board[row][col] = "."
                    rows[row].discard(num)
                    cols[col].discard(num)
                    boxes[box].discard(num)

            to_visit.append((row, col))
            return False

        backtrack()


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
obj = Solution()
print(obj.solveSudoku(board))
