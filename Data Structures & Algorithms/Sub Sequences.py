from functools import cache


class Subsequences:
    """
    Subsequence of a string.

    Ex: Sub sequence of "abc" are
        a, b, c, ab, ac, bc, abc, ""
    """

    def __init__(self, s: str) -> None:
        self.ans = []
        self.s = s

    def get(self) -> list[str]:
        self.generate(self.s)
        return self.ans

    @cache
    def generate(self, input: str, output: str = "") -> None:
        """
        generate subsequences
        """

        # if the input is empty append the output string
        if len(input) == 0:
            self.ans.append(output)
            return

        # output is passed with including the
        # 1st character of input string
        self.generate(input[1:], output + input[0])

        # output is passed without including the
        # 1st character of input string
        self.generate(input[1:], output)


# obj = Subsequences("abc")
# print(obj.get())


class PalindromicSubsequence:
    """
    Generate palindromic sub subsequence of a string

    Ex: abc
    Palindromic sub sequence are: a, b, c

    aaa => a, a, a, aa, aa, aa, aaa
    """

    def __init__(self, s: str) -> None:
        self.ans = []
        self.s = s

    def get(self) -> list[str]:
        self.generate(self.s)
        return self.ans

    @cache
    def generate(self, input: str, output: str = "") -> None:
        """
        generate palindromic subsequences
        """

        # if input is empty
        # check if output has value and
        # if it is a palindrome
        # then append it to ans
        if len(input) == 0:
            if output and output == output[::-1]:
                self.ans.append(output)
            return

        # output is passed with including the
        # 1st character of input string
        self.generate(input[1:], output + input[0])

        # output is passed without including the
        # 1st character of input string
        self.generate(input[1:], output)


# obj = PalindromicSubsequence("abc")
# print(obj.get())


class LongestPalindromicSubsequence:
    """
    Return the length of the longest palindromic subsequence

    Ex: "bbbab" => "bbbb"
        "cbbd" => "bb"

    Solution:

    We will check from start to end of chars.

        1.  If left and right are same,
            it means we get 1 length char which is palindrome.

        2.  If left > right,
            it means index is out of bound.
            So we return 0.

        3.  If left and right index char are same,
            it means we get 2 same char which are palindrome
            and with these 2 chars we get 2 chars in total.

            So, we will return 2 and also call the function
            for next left and right.

        4.  Else we will once increase left index
            and once decrease right index.

    """

    def __init__(self, s: str) -> None:
        self.s = s

    def get(self):
        return self.generate(0, len(self.s) - 1)

    @cache
    def generate(self, left: int, right: int) -> int:
        if left == right:
            return 1

        if left > right:
            return 0

        if self.s[left] == self.s[right]:
            return 2 + self.generate(left + 1, right - 1)

        return max(self.generate(left + 1, right), self.generate(left, right - 1))


# obj = LongestPalindromicSubsequence("bbbab")
# print(obj.get())


class CountPalindromicSubsequences:
    """
    Leet Code Problem:  730 Count Different Palindromic Subsequences
    Link:   https://leetcode.com/problems/count-different-palindromic-subsequences/

    Problem:
        Given a string s, return the number of different non-empty palindromic subsequences in s.

    Solution:

        1.  We traverse within a range, starting from 0 to end.

        2.  We will check if from current start to end if there is
            any "abcd" contains.
            If contains then we will get the range of them.

        3.  We can get many palindrome from the range if
            all condition passes.

    """

    def get(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        return self.generate(s, 0, len(s)) % MOD

    @cache
    def generate(self, s: str, start: int, end: int) -> int:
        # If start == end, it means we have exceeded our limit.
        if start >= end:
            return 0

        count = 0

        for char in "abcd":
            # get the left and right index of char from string
            left, right = s.find(char, start, end), s.rfind(char, start, end)

            # if these both are -1, it means there is no char in string
            if left == -1 or right == -1:
                continue

            # If left == right it means we are pointing same char
            # So we add 1
            if left == right:
                count += 1

            # Else we have found 2 char
            # So we add 2 and call next chars
            else:
                count += 2 + self.generate(s, left + 1, right)

        return count


obj = CountPalindromicSubsequences()
print(obj.get("cbcb"))  # 6