import operator
from functools import reduce
import itertools
from unittest import result


def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
    """
    Time limit exceeded
    """
    return [reduce(lambda x, y: x ^ y, arr[idx[0] : idx[1] + 1]) for idx in queries]


def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
    sums = list(itertools.accumulate(arr, func=operator.ixor)) + [0]
    return [sums[val] ^ sums[idx - 1] for idx, val in queries]


def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
    prefixXor = [0] * (len(arr) + 1)
    for i, a in enumerate(arr):
        prefixXor[i + 1] = prefixXor[i] ^ a
    return [(prefixXor[q + 1] ^ prefixXor[p]) for p, q in queries]


print(xorQueries(0, [1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]]))
print(xorQueries(0, [4, 8, 2, 10], [[2, 3], [1, 3], [0, 0], [0, 3]]))
