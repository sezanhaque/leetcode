import itertools


def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    hashmap = {}
    for word in strs:
        key = "".join(sorted(word))
        if key in hashmap:
            hashmap[key].append(word)
        else:
            hashmap[key] = [word]
    # return [v for _, v in hashmap.items()]
    return list(hashmap.values())


def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    groups = itertools.groupby(sorted(strs, key=sorted), sorted)
    return [sorted(members) for _, members in groups]


print(groupAnagrams(0, ["eat", "tea", "tan", "ate", "nat", "bat"]))
# print(groupAnagrams(0, []))
# print(groupAnagrams(0, ["a"]))
