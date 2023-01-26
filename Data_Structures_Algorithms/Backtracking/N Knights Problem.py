class Solution:
    """
    Given a N x N matrix board.
    We need to determine how many ways we can place N number of Knights in the board.

    In chess game, a Knight can travel from the current place to
        1.  top -> top -> left (row - 2, col - 1)
        2.  top -> left -> left (row - 1, col - 2)
        3.  top -> top -> right (row - 2, col + 1)
        4.  top -> left -> right (row - 1, col + 2)

        5.  bottom -> bottom -> left (row + 2, col - 1)
        6.  bottom -> left -> left (row + 1, col - 2)
        7.  bottom -> bottom -> right (row + 2, col + 1)
        8.  bottom -> left -> right (row + 1, col + 2)

    We will move from 0,0 block of the block to end to check where can
    we place the Knight. If a previous Knight face the new Knight path then
    we can not place the new Knight in that block.

    So, we can check from current block to:
        1.  top -> top -> left (row - 2, col - 1)
        2.  top -> left -> left (row - 1, col - 2)
        3.  top -> top -> right (row - 2, col + 1)
        4.  top -> left -> right (row - 1, col + 2)

    as there will be no Knight below the current row.
    """

    def __init__(self, n: int):
        self.board = [[False for j in range(n)] for i in range(n)]
        self.n = n

    def knight(self, row: int, col: int, knights: int) -> None:
        if knights == 0:
            self.display()
            print("")
            return

        # we reach to the down of the board, so return
        if row == len(self.board) - 1 and col == len(self.board[0]):
            return

        # we reach to the max column of current row
        # so go to the next row
        if col == len(self.board):
            self.knight(row + 1, 0, knights)
            return

        # if current block is safe to travel then we are
        # going to next column, subtracting the knights by 1
        # and marking the current block as true for backtracking
        # purpose after that we are reverting it to false
        if self.isSafe(row, col):
            self.board[row][col] = True
            self.knight(row, col + 1, knights - 1)
            self.board[row][col] = False

        # else we go to the next column without
        self.knight(row, col + 1, knights)

    def display(self) -> None:
        """
        Display the board after placing the knights
        """
        for row in self.board:
            for block in row:
                if block:
                    print("K ", end="")
                else:
                    print("* ", end="")
            print("")

    def isSafe(self, row: int, col: int) -> bool:
        """
        Check if the current block is safe for knight

        We will check starting from the current block to:
            1.  top -> top -> left (row - 2, col - 1)
            2.  top -> left -> left (row - 1, col - 2)
            3.  top -> top -> right (row - 2, col + 1)
            4.  top -> left -> right (row - 1, col + 2)

        If we find any knight in these paths then we will return false else true.
        """

        # 2 top 1 left: row - 2, col - 1
        if self.isValid(row - 2, col - 1):
            if self.board[row - 2][col - 1]:
                return False

        # 1 top 2 left: row - 1, col - 2
        if self.isValid(row - 1, col - 2):
            if self.board[row - 1][col - 2]:
                return False

        # 2 top 1 right: row - 2, col + 1
        if self.isValid(row - 2, col + 1):
            if self.board[row - 2][col + 1]:
                return False

        # 1 top 2 right: row - 1, col + 2
        if self.isValid(row - 1, col + 2):
            if self.board[row - 1][col + 2]:
                return False

        return True

    def isValid(self, row: int, col: int) -> bool:
        """
        Check if current block is in the board.
        """
        if 0 <= row < len(self.board) and 0 <= col < len(self.board[0]):
            return True

        return False


if __name__ == "__main__":
    n = 4
    obj = Solution(4)
    print(obj.knight(0, 0, n))
