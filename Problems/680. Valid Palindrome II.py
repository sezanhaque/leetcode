def validPalindrome(self, s: str) -> bool:
    if s == s[::-1]:
        return True
    length = len(s)
    i = 0
    while i < length // 2 and s[i] == s[length - 1 - i]:
        i += 1
    test_1 = s[:i] + s[i + 1 :]
    test_2 = s[: length - 1 - i] + s[length - 1 - i + 1 :]
    return test_1 == test_1[::-1] or test_2 == test_2[::-1]


print(validPalindrome(0, "adymda"))
print("*" * 50)
print(validPalindrome(0, "aba"))
print("*" * 50)
print(validPalindrome(0, "abca"))
print("*" * 50)
print(validPalindrome(0, "abc"))
print("*" * 50)
print(validPalindrome(0, "dddde"))
print("*" * 50)
print(validPalindrome(0, "deeee"))
