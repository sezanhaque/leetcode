def guessNumber(self, n: int) -> int:
    left, right = 1, n
    while left <= right:
        # mid = (left + right) // 2
        mid = (left + right) >> 1
        pick = guess(mid)
        print(left, right, mid, pick)
        if pick == 0:
            return mid
        elif pick == 1:
            left = mid + 1
        else:
            right = mid - 1
    return left


def guessNumber(self, n: int) -> int:
    left, right = 1, n
    # Binary division faster than (left + right) // 2
    myGuess = (left + right) >> 1
    """
    "walrus" operator ':=' - assigns value of the function to the variable 'res'
	and then compare res with 0
    """
    while (res := guess(myGuess)) != 0:
        if res == 1:
            left = myGuess + 1
        else:
            right = myGuess - 1
        myGuess = (left + right) >> 1
    return myGuess


def guess(num: int) -> int:
    pick = 6
    if num == pick:
        return 0
    elif num > pick:
        return -1
    else:
        return 1


print(guessNumber(0, 10))
