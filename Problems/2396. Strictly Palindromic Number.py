import string


def isStrictlyPalindromic(self, n: int) -> bool:
    def int2base(self, x, base):
        if x < 0:
            sign = -1
        elif x == 0:
            return digs[0]
        else:
            sign = 1

        x *= sign
        digits = []

        while x:
            digits.append(digs[x % base])
            x = x // base

        if sign < 0:
            digits.append("-")

        digits.reverse()

        return "".join(digits)

    digs = n
    digs = string.digits + string.ascii_letters
    for i in range(2, n - 1):
        getBase = int2base(0, n, i)
        if getBase != getBase[::-1]:
            return False


def isStrictlyPalindromic(self, n: int) -> bool:
    def is_palindrome(self, s):
        return s == s[::-1]

    def base_rep(self, num, base):
        result = ""
        while num != 0:
            reminder = num % base
            num = num // base
            result = result + str(reminder)
        return result[::-1]

    return all([is_palindrome(0, base_rep(0, n, base)) for base in range(2, n - 1)])

# def isStrictlyPalindromic(self, n: int) -> bool:
#     """
#     Always answer will be False
#     """
#     return False

print(isStrictlyPalindromic(0, 9))
