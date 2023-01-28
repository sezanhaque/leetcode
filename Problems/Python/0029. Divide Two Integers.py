class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        pos_dividend, pos_divisor, res = abs(dividend), abs(divisor), 0

        for num in range(32)[::-1]:
            # dividend // num - divisor
            if (pos_dividend >> num) - pos_divisor >= 0:
                # res += 1 * 2 * num
                res += 1 << num

                # dividend -= divisor * 2 * num
                pos_dividend -= pos_divisor << num

        return res if (dividend > 0) == (divisor > 0) else -res

    def divide(self, dividend: int, divisor: int) -> int:
        # https://leetcode.com/problems/divide-two-integers/solutions/1516367/complete-thinking-process-intuitive-explanation-all-rules-followed-c-code/

        # dividend = (quotient) * divisor + remainder

        # if either of them are neg
        is_negative = (dividend < 0) != (divisor < 0)
        divisor, dividend = abs(divisor), abs(dividend)

        quotient = 0
        the_sum = divisor

        while the_sum <= dividend:
            current_quotient = 1

            # the_sum * 2
            while (the_sum << 1) <= dividend:
                the_sum <<= 1

                # current_quotient * 2
                current_quotient <<= 1

            dividend -= the_sum
            the_sum = divisor
            quotient += current_quotient

        return min(2147483647, max(-quotient if is_negative else quotient, -2147483648))


obj = Solution()
print(obj.divide(dividend=10, divisor=3))
