import re


def isPalindrome(self, s: str) -> bool:
    """Most Effective Solution"""
    result = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
    for i in range(len(result) // 2):
        if result[i] != result[-i - 1]:
            return False
    return True


def isPalindrome(self, s: str) -> bool:
    s = [c for c in s.lower() if c.isalnum()]
    return s == s[::-1]
    # return list(reversed(s)) == s


print(isPalindrome(0, "A man, a plan, a canal: Panama"))
print(isPalindrome(0, "race a car"))
print(isPalindrome(0, " "))
