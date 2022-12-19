import string


class Solution:
    """
    Explanation:
        For each palindrome in format of "aba",
        we enumerate the character on two side.

        We find its first occurrence and its last occurrence,
        all the characters in the middle are the candidate for the midd char.


    Complexity:
        Time O(26n)
        Space O(26n)
    """
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0

        # loop through every character from a-z
        for char in string.ascii_lowercase:
            # find the index of char
            left, right = s.find(char), s.rfind(char)

            # find out how many unique char are in between left and right
            # as left and right will be same char
            # so every oder char in the middle will make a 3 length palindromic subsequence
            if left >= 0:
                res += len(set(s[left + 1: right]))

        return res


print(Solution.countPalindromicSubsequence(0, "aabca"))

