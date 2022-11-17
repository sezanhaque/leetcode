"""
    This is easy to understand by following an example.
    Consider the fraction 611/4950 == 0.12(34).
    If you work out the division, you'll see that the
    remainders are 611, 1160, 1700, 2150, 1700, 2150, etc.

        0.123434...
        +---------
    4950|611
        0
        ---------
        6110      <- remainder is 611
        4950
        ---------
        11600     <- remainder is 1160
        9900
        ---------
        17000    <- remainder is 1700
        14850
        ---------
        21500   <- remainder is 2150
        19800
        ---------
            17000  <- remainder is 1700
            14850
        ---------
            21500 <- remainder is 2150
            19800
        ---------
            1700 <- remainder is 1700
            ...

    So we just have to keep track of the remainders. 
    The moment we see a repeated one (1700 in this example), 
    we stop and ask "when was the first time I saw this remainder?" 
    For this particular example, the answer is "when I was trying 
    to find the 3rd decimal place". Therefore, the recurrence 
    starts from the 3rd decimal place. That's it.
"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)

        # If numerator, denominator are negative, we make positive
        p, q = map(abs, (numerator, denominator))

        # Everything before the decimal point
        prefix = (
            ("" if (numerator > 0) == (denominator > 0) else "-") + str(p // q) + "."
        )

        # Everything after the decimal point
        suffix = ""
        seen = {}
        remainder = p % q

        # search for recurrence
        while remainder not in seen:
            seen[remainder] = len(suffix)
            remainder *= 10
            suffix += str(remainder // q)
            remainder %= q

            # it means no repetition
            if remainder == 0:
                return prefix + suffix
        return (
            prefix + suffix[: seen[remainder]] + "(" + suffix[seen[remainder] :] + ")"
        )


print(Solution.fractionToDecimal(0, numerator=1, denominator=2))
print(Solution.fractionToDecimal(0, numerator=2, denominator=1))
print(Solution.fractionToDecimal(0, numerator=4, denominator=333))
