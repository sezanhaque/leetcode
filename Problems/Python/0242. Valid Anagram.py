def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    for i in t:
        if i not in s:
            return False
    return True


def isAnagramSlow(self, s: str, t: str) -> bool:
    """Slow"""
    if len(s) != len(t):
        return False
    s_dict = {}
    t_dict = {}
    while s or t:
        if s:
            s_dict[s[0]] = s_dict.get(s[0], 0) + 1
            s = s[1:]
        if t:
            t_dict[t[0]] = t_dict.get(t[0], 0) + 1
            t = t[1:]
    return s_dict == t_dict


def isAnagram(self, s: str, t: str) -> bool:
    """Fast"""
    if len(s) != len(t):
        return False
    s_dict, t_dict = {}, {}
    for i in s:
        if i in s_dict:
            s_dict[i] += 1
        else:
            s_dict[i] = 1
    for i in t:
        if i in t_dict:
            t_dict[i] += 1
        else:
            t_dict[i] = 1
    for i in s_dict:
        if i not in t_dict:
            return False
        if s_dict[i] != t_dict[i]:
            return False
    return True


def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_dict, t_dict = {}, {}

    for i in range(len(s)):
        if s[i] in s_dict:
            s_dict[s[i]] += 1
        else:
            s_dict[s[i]] = 1
        if t[i] in t_dict:
            t_dict[t[i]] += 1
        else:
            t_dict[t[i]] = 1
    return s_dict == t_dict


def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


print(isAnagram(0, "anagram", "nagaram"))
print(isAnagram(0, "rat", "cat"))
print(isAnagram(0, "aacc", "ccac"))
