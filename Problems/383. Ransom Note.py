from collections import Counter


def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    magazine_dict, ransomNote_dict = {}, {}

    for letter in magazine:
        if letter in magazine_dict:
            magazine_dict[letter] += 1
        else:
            magazine_dict[letter] = 1

    for letter in ransomNote:
        if letter in ransomNote_dict:
            ransomNote_dict[letter] += 1
        else:
            ransomNote_dict[letter] = 1

    for letter in ransomNote_dict:
        if letter not in magazine_dict:
            return False
        if ransomNote_dict[letter] > magazine_dict[letter]:
            return False
    return True


def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    for i in set(ransomNote):
        if ransomNote.count(i) > magazine.count(i):
            return False
    return True


def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    return not Counter(ransomNote) - Counter(magazine)


print(canConstruct(0, "aa", "aab"))
# print(canConstruct(0, "aa", "ab"))
# print(canConstruct(0, "a", "b"))
# print(canConstruct(0, "aab", "baa"))
print(canConstruct(0, "bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))
