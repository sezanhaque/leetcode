import enum
from math import inf


def numberOfWays(row: int, col: int) -> int:
    """
    Get the number of ways for a maze where row and column is given.

    We can move from left to right or left to down.
    """

    # If row / col == 1 then we are in the edge of the maze
    # So we have only one path remaining to go to the destination
    # Either it will be from down to right / from right to down
    # So return 1
    if row == 1 or col == 1:
        return 1

    # We are going right
    right = numberOfWays(row - 1, col)

    # We are going down
    down = numberOfWays(row, col - 1)

    return right + down


# print("*" * 20 + " Get the number of ways for a maze where row and column is given " + "*" * 20)
# print(numberOfWays(3, 3))
# print("*" * 20 + " Get the number of ways for a maze where row and column is given " + "*" * 20 + "\n\n")


def numberOfPathDiagonal(row: int, col: int) -> list[str]:
    """
    Get the number of path for a maze where row and column is given.

    We can move from left to right or left to down and diagonal also.
    """
    res = []

    def DFS(path: str, row: int, col: int):
        # If row, col == 1, 1 it means we are in the edge of the maze
        # So append the path to the array and return.
        if row == 1 and col == 1:
            return res.append(path[:len(path) - 2])

        # We are going down / Vertical
        if row > 1:
            DFS(path + "V->", row - 1, col)

        # We are going right / horizontal
        if col > 1:
            DFS(path + "H->", row, col - 1)

        # We are going diagonal
        if row > 1 and col > 1:
            DFS(path + "D->", row - 1, col - 1)

    DFS("", row, col)
    return res


# print("*" * 20 + " Get the paths with diagonal for a maze where row and column is given " + "*" * 20)
# print(numberOfPathDiagonal(3, 3))
# print("*" * 20 + " Get the paths with diagonal for a maze where row and column is given " + "*" * 20 + "\n\n")


def pathRestrictions(maze: list[list[int]]) -> list[str]:
    """
    Get the number of path for a maze where restriction is given.

    We can move from left to right or left to down and diagonal also.
    But if we face any restriction or obstetrical then we will skip.
    """
    res = []

    def DFS(path: str, row: int, col: int):
        # If row, col == 1, 1 it means we are in the edge of the maze
        # So append the path to the array and return.
        if row == len(maze) - 1 and col == len(maze[0]) - 1:
            return res.append(path[:len(path) - 2])

        # if the block is restricted then we ignore it
        if not maze[row][col]:
            return

        # We are going down / Vertical
        if row < len(maze) - 1:
            DFS(path + "V->", row + 1, col)

        # We are going right / horizontal
        if col < len(maze[0]) - 1:
            DFS(path + "H->", row, col + 1)

        # We are going diagonal
        if row < len(maze) - 1 and col < len(maze[0]) - 1:
            DFS(path + "D->", row + 1, col + 1)

    DFS("", 0, 0)
    return res


# print("*" * 20 + " Get the paths with restriction for a maze where row and column is given " + "*" * 20)
# maze = [[True] * 3,
#         [True, False, True],
#         [True] * 3]
# print(pathRestrictions(maze))
# print(
#     "*" * 20 + " Get the paths with restriction for a maze where row and column is given " + "*" * 20 + "\n\n")


def allPath(maze: list[list[int]]) -> list[str]:
    """
    Get the number of path for a maze, print all path.

    We can move from any way within the range.
    """
    res = []

    def DFS(path: str, row: int, col: int):
        # If row, col == 1, 1 it means we are in the edge of the maze
        # So append the path to the array and return.
        if row == len(maze) - 1 and col == len(maze[0]) - 1:
            return res.append(path[:len(path) - 2])

        # if the block is restricted then we ignore it
        if not maze[row][col]:
            return

        # making the current block to false
        # so that we won't visit it again and again
        maze[row][col] = False

        # We are going down / Vertical
        if row < len(maze) - 1:
            DFS(path + "V->", row + 1, col)

        # We are going right / horizontal
        if col < len(maze[0]) - 1:
            DFS(path + "H->", row, col + 1)

        # We are going up
        if row > 0:
            DFS(path + "U->", row - 1, col)

        # We are going left
        if col > 0:
            DFS(path + "L->", row, col - 1)

        # We are going diagonal
        # if row < len(maze) - 1 and col < len(maze[0]) - 1:
        #     DFS(path + "D->", row + 1, col + 1)

        # reverting the current block to true
        maze[row][col] = True

    DFS("", 0, 0)
    return res


# print("*" * 20 + " Get all path for a maze " + "*" * 20)
# maze = [[True, True, True],
#         [True, True, True],
#         [True, True, True]]
# print(allPath(maze))
# print(
#     "*" * 20 + " Get all path for a maze " + "*" * 20 + "\n\n")


def allPathPrint(maze: list[list[int]]) -> None:
    """
    Get the number of path for a maze, print all path with list.

    We can move from any way within the range.
    """
    steps = [[0] * len(maze[0]) for i in range(len(maze))]

    def DFS(path: str, row: int, col: int, step: int):
        # If row, col == 1, 1 it means we are in the edge of the maze
        # So append the path to the array and return.
        if row == len(maze) - 1 and col == len(maze[0]) - 1:
            steps[row][col] = step

            # print steps
            for s in steps:
                print(s)

            # print paths
            print(path[:len(path) - 2])

            return

        # if the block is restricted then we ignore it
        if not maze[row][col]:
            return

        # making the current block to false
        # so that we won't visit it again and again
        maze[row][col] = False

        # store the current step to steps list
        steps[row][col] = step

        # We are going down / Vertical
        if row < len(maze) - 1:
            DFS(path + "V->", row + 1, col, step + 1)

        # We are going right / horizontal
        if col < len(maze[0]) - 1:
            DFS(path + "H->", row, col + 1, step + 1)

        # We are going up
        if row > 0:
            DFS(path + "U->", row - 1, col, step + 1)

        # We are going left
        if col > 0:
            DFS(path + "L->", row, col - 1, step + 1)

        # We are going diagonal
        # if row < len(maze) - 1 and col < len(maze[0]) - 1:
        #     DFS(path + "D->", row + 1, col + 1)

        # reverting the current block to true
        maze[row][col] = True

        # change the block to 0
        steps[row][col] = 0

    DFS("", 0, 0, 0)


# print("*" * 20 + " Print all path with restriction for a maze " + "*" * 20)
# maze = [[True, True, True, True, True],
#         [True, False, False, False, True],
#         [True, True, True, False, True],
#         [True, False, True, False, True],
#         [True, True, True, True, True]]
#
# allPathPrint(maze)
# print(
#     "*" * 20 + " Print all path with restriction for a maze " + "*" * 20 + "\n\n")

def allPathPrintWithArrow(maze: list[list[int]]) -> None:
    """
    Get the number of path for a maze, print all path with list.

    We can move from any way within the range.
    """

    class SIGNS(str, enum.Enum):
        start = "✔"
        end = "🚫"
        left = "⬅"
        right = "➡"
        up = "⬆"
        down = "⬇"
        diagonal = "↘"

    steps = [["."] * len(maze[0]) for i in range(len(maze))]

    def DFS(path: str, row: int, col: int, step: str):
        # If row, col == 1, 1 it means we are in the edge of the maze
        # So append the path to the array and return.
        if row == len(maze) - 1 and col == len(maze[0]) - 1:
            steps[row][col] = SIGNS.end.value

            # print steps
            for s in steps:
                print(s)

            # print paths
            print(path[:len(path) - 2])

            return

        # if the block is restricted then we ignore it
        if not maze[row][col]:
            return

        # making the current block to false
        # so that we won't visit it again and again
        maze[row][col] = False

        # store the current step to steps list
        steps[row][col] = step

        # We are going down / Vertical
        if row < len(maze) - 1:
            DFS(path + "V->", row + 1, col, SIGNS.down.value)

        # We are going right / horizontal
        if col < len(maze[0]) - 1:
            DFS(path + "H->", row, col + 1, SIGNS.right.value)

        # We are going up
        if row > 0:
            DFS(path + "U->", row - 1, col, SIGNS.up.value)

        # We are going left
        if col > 0:
            DFS(path + "L->", row, col - 1, SIGNS.left.value)

        # We are going diagonal
        if row < len(maze) - 1 and col < len(maze[0]) - 1:
            DFS(path + "D->", row + 1, col + 1, SIGNS.diagonal.value)

        # reverting the current block to true
        maze[row][col] = True

        # change the block to 0
        steps[row][col] = "."

    DFS("", 0, 0, SIGNS.start.value)


# print("*" * 20 + " Print all path with arrow with restriction for a maze " + "*" * 20)
# maze = [[True, True, True, True, True],
#         [True, False, False, False, True],
#         [True, True, True, False, True],
#         [True, False, True, False, True],
#         [True, True, True, True, True]]
#
# allPathPrintWithArrow(maze)
# print(
#     "*" * 20 + " Print all path with arrow with restriction for a maze " + "*" * 20 + "\n\n")


def shortestPathCost(maze: list[list[int]]) -> str:
    """
    Get the shortest path from starting of a maze to end.

    We can move from any way within the range.
    """
    res = ""

    def DFS(path: str, row: int, col: int):
        nonlocal res

        # If row, col == 1, 1 it means we are in the edge of the maze
        # So append the path to the array and return.
        if row == len(maze) - 1 and col == len(maze[0]) - 1:
            # if res is empty or len of res is less than path
            # then update the res
            # and always return to terminate the recursion
            if not res or len(res) > len(path):
                res = path
            return

        if not maze[row][col]:
            return

        # making the current block to false
        # so that we won't visit it again and again
        maze[row][col] = False

        # We are going down / Vertical
        if row < len(maze) - 1:
            DFS(path + "V", row + 1, col)

        # We are going right / horizontal
        if col < len(maze[0]) - 1:
            DFS(path + "H", row, col + 1)

        # We are going up
        if row > 0:
            DFS(path + "U", row - 1, col)

        # We are going left
        if col > 0:
            DFS(path + "L", row, col - 1)

        # We are going diagonal
        # if row < len(maze) - 1 and col < len(maze[0]) - 1:
        #     DFS(path + "D", row + 1, col + 1)

        # reverting the current block to true
        maze[row][col] = True

    DFS("", 0, 0)
    return res


print("*" * 20 + " Get the shortest path from starting of a maze to end " + "*" * 20)
maze = [[True, True, True],
        [True, True, True],
        [True, True, True]]
print(shortestPathCost(maze))
print(
    "*" * 20 + " Get the shortest path from starting of a maze to end " + "*" * 20 + "\n\n")
