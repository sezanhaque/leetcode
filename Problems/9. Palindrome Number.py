def isPalindrome(self, x: int) -> bool:
    return str(x) == str(x)[::-1]


print(isPalindrome(0, 121))
print(isPalindrome(0, 123))
print(isPalindrome(0, -123))
print(isPalindrome(0, 10))
