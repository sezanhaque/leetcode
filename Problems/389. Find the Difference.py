""""
Solution:
s = abcd
t = abcde

if we take XOR of every character. all the n character of s "abcd" is similar to n character of t "abcd". So, they will cancel each other. 
And we left with our answer.

s =   abcd
t =   abcde
------------
ans -> e
-----------
"""


def findTheDifference(self, s: str, t: str) -> str:
    """Iterate through both string and XOR the characters"""
    difference = 0
    for i in range(len(s)):
        difference ^= ord(s[i])

    for i in range(len(t)):
        difference ^= ord(t[i])
    return chr(difference)


def findTheDifference(self, s: str, t: str) -> str:
    """Fastest solution"""
    difference = 0
    """
    Combine the S & T with sorting string into one string 
    and then XOR the characters together
    """
    for char in s + t:
        difference ^= ord(char)
    return chr(difference)


print(findTheDifference(0, "abcd", "abcde"))
print(findTheDifference(0, "", "y"))
print(findTheDifference(0, "a", "aa"))
