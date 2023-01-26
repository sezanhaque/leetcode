class Solution:
    """
    Given a N x N matrix board.
    We need to determine how many ways we can place N number of Queens in the board.

    In chess game, a Queen can travel from the current place to
        Left, Right, Up, Down, Diagonal Left, Diagonal Right

    We will move from 0,0 block of the block to end to check where can
    we place the Queen. If a previous Queen face the new Queen path then
    we can not place the new Queen in that block.

    So, we can check from current block to Up, Diagonal Left, Diagonal Right
    as there will be no Queen below the current row.
    """

    def __init__(self, n: int):
        self.board = [[False for j in range(n)] for i in range(n)]
        self.n = n

    def display(self) -> None:
        """
        Display the board after placing the queens
        """
        for row in self.board:
            for block in row:
                if block:
                    print("Q ", end="")
                else:
                    print("* ", end="")
            print("")

    def isSafe(self, row: int, col: int) -> bool:
        """
        Check if the current block is safe for queen

        We will check starting from the current block to:
            1.  top
            2.  diagonal left
            3.  diagonal right

        If we find any queen in these paths then we will return false else true.
        """

        # check vertical / up row
        for i in range(row):
            # if the block is true then it has a queen
            # return false
            if self.board[i][col]:
                return False

        # check diagonal left
        maxLeft = min(row, col)
        for i in range(1, maxLeft + 1):
            if self.board[row - i][col - i]:
                return False

        # check diagonal right
        maxRight = min(row, len(self.board[0]) - col - 1)
        for i in range(1, maxRight + 1):
            if self.board[row - i][col + i]:
                return False

        return True

    def queens(self, row: int) -> int:
        if row == len(self.board):
            self.display()
            print("")
            return 1

        count = 0

        # placing the queen and checking every row and col
        for col in range(len(self.board[0])):
            # place the queen if it is safe
            if self.isSafe(row, col):
                self.board[row][col] = True
                # go to the next row and check
                # if it is possible to place the queen
                # if so then return count and add it
                # to count
                count += self.queens(row + 1)
                self.board[row][col] = False

        return count


if __name__ == "__main__":
    n = 4
    obj = Solution(n)
    print(obj.queens(0))
