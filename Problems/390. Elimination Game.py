def lastRemaining(self, n: int) -> int:
    """
    This solution solves all test cases but
    memory limit exceeded on the last test case
    """
    arr = [i for i in range(1, n + 1)]
    count = 1
    length = len(arr)

    while length > 1:
        new_arr = []
        if count % 2 != 0:
            i, idx = 0, 0
            while i + 1 < length:
                new_arr.append(arr[i + 1])
                idx += 1
                i += 2
        else:
            i = length - 1
            while i > 0:
                new_arr.append(arr[i - 1])
                i -= 2
            new_arr = new_arr[::-1]
        count += 1
        length //= 2
        arr = new_arr
    return arr[0]


def lastRemaining(self, n: int) -> int:
    """
    Every time our "n" is getting halved (n // 2).
    We notice that if we take out 2 common, all the patterns are same

    First Step : 1, 2, 3, 4, 5, 6, 7, 8, 9 when n = 9
    Second Step : 2 x [1,2,3,4] = [2, 4, 6, 8]
    Third Step : 2x [1,3] = [2, 6]

    We just need to take care about the iteration with odd length,
    so we add a 1 in the end. Odd + 1 = Even.
    """
    return 1 if n == 1 else 2 * (n // 2 - lastRemaining(0, n // 2) + 1)


print(lastRemaining(0, 10))
