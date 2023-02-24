class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        length = len(s)
        i = 0

        while i < length >> 1 and s[i] == s[~i]:
            i += 1

        # skip ith char
        test_1 = s[:i] + s[i + 1:]

        # add ith char and skip i+1-th char
        # length - 1 - i == ~i but
        # length - 1 - i + 1 != ~i + 1
        test_2 = s[: ~i] + s[length - 1 - i + 1:]

        # check if test_1 or test_2 is palindrome
        return test_1 == test_1[::-1] or test_2 == test_2[::-1]


obj = Solution()
print(obj.validPalindrome("adymda"))  # true
print("*" * 50)
print(obj.validPalindrome("aba"))  # true
print("*" * 50)
print(obj.validPalindrome("abca"))  # true
print("*" * 50)
print(obj.validPalindrome("abc"))  # false
print("*" * 50)
print(obj.validPalindrome("dddde"))  # true
print("*" * 50)
print(obj.validPalindrome("deeee"))  # true
print("*" * 50)
print(obj.validPalindrome("eccer"))  # true
