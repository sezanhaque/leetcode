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


obj = LongestPalindromicSubsequence("bbbab")
print(obj.get())
