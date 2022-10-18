import collections


def frequencySort(self, s: str) -> str:
    count = collections.Counter(s)
    sorted_str = sorted(sorted(s), key=lambda x: (count[x]), reverse=True)
    return "".join(sorted_str)


def frequencySort(self, s: str) -> str:
    """
    Fastest Solution
    """
    result = []
    count = collections.Counter(s)
    for key, value in count.most_common():
        result.append(key * value)

    return "".join(result)


print(frequencySort(0, "tree"))
print(frequencySort(0, "cccaaa"))
print(frequencySort(0, "Aabb"))
print(frequencySort(0, "eeeelolovtcd"))
