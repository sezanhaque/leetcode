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


print(groupAnagrams(0, ["eat", "tea", "tan", "ate", "nat", "bat"]))
# print(groupAnagrams(0, []))
# print(groupAnagrams(0, ["a"]))
