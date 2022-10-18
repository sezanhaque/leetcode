from collections import Counter


def mostFrequentEven(self, nums: list[int]) -> int:
    repeat = Counter(x for x in nums if not x & 1)
    best = -1
    result = -1

    for i in nums:
        if not i & 1:   # i % 2
            if repeat[i] > best or (repeat[i] == best and i < result):
                best = repeat[i]
                result = i

    return result


def mostFrequentEven(self, nums: list[int]) -> int:
    count_occurrence = Counter(x for x in nums if x & 1 == 0)
    return min(count_occurrence, key=lambda x: (-count_occurrence[x], x), default=-1)


print(mostFrequentEven(0, [0, 1, 2, 0, 0, 0, 2, 4, 4, 1]))
# print(mostFrequentEven(0, [0, 1, 2, 2, 4, 4, 1, 6, 6]))
# print(mostFrequentEven(0, [4, 4, 4, 9, 2, 4]))
# print(mostFrequentEven(0, [29, 47, 21, 41, 13, 37, 25, 7]))
# print(mostFrequentEven(0, [0, 0, 0, 0]))
print(
    mostFrequentEven(
        0, [8154, 9139, 8194, 3346, 5450, 9190, 133, 8239, 4606, 8671, 8412, 6290]
    )
)
