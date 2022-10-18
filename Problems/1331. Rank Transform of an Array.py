def arrayRankTransform(self, arr: list[int]) -> list[int]:
    sorted_arr = sorted(arr)
    result = []
    count = 0
    dict = {}

    for val in sorted_arr:
        if val not in dict:
            dict[val] = count + 1
            count += 1

    for val in arr:
        result.append(dict.get(val))

    return result


def arrayRankTransform(self, arr: list[int]) -> list[int]:
    rank = {}
    for val in sorted(arr):
        rank.setdefault(val, len(rank) + 1)

    return map(rank.get, arr)


def arrayRankTransform(self, arr: list[int]) -> list[int]:
    return map({val: idx + 1 for idx, val in enumerate(sorted(set(arr)))}.get, arr)


print(arrayRankTransform(0, [40, 10, 20, 30]))
print(arrayRankTransform(0, [100, 100, 100]))
print(arrayRankTransform(0, [37, 12, 28, 9, 100, 56, 80, 5, 12]))
