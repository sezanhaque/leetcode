from math import inf


def minimumRecolors(self, blocks: str, k: int) -> int:
    min_operation, step = 0, 0
    while step < len(blocks) - k + 1:
        """
        While our current step / index is less then (length - number of blocks "k" - 1)
            1. define a temporary array which will contain only from the step to "k" index characters
            2. count the number of "W" in temp array and compare the number with previous min_operation

        *** you can also define min_operation = inf if you want
            then you won't have to check "if step == 0" and you can directly use
            "min_operation = min(min_operation, temp_arr.count("W"))"
            and remove the if else condition
        ***
        """
        temp_arr = blocks[step : step + k]
        if step == 0:
            min_operation += temp_arr.count("W")
        else:
            min_operation = min(min_operation, temp_arr.count("W"))
        step += 1

    return min_operation


def minimumRecolors(self, blocks: str, k: int) -> int:
    min_operation, step = inf, 0
    while step < len(blocks) - k + 1:
        temp_arr = blocks[step : step + k]
        min_operation = min(min_operation, temp_arr.count("W"))
        step += 1

    return min_operation


print(minimumRecolors(0, "WBBWWBBWBW", 7))
print(minimumRecolors(0, "WBWBBBW", 2))
print(minimumRecolors(0, "BWWWBB", 6))
