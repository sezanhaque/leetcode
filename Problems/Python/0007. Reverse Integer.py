def reverse(self, x: int) -> int:
    """
    Hex(-2**31-1), hex(2**31-1) limit of signed integer
    The intervals 0 to (2^31)-1 and (-2^31) to 0
    """
    neg_limit, pos_limit = -0x80000000, 0x7FFFFFFF  
    if x < 0:
        reverse_number = -int(str(abs(x))[::-1])
        if reverse_number & neg_limit == neg_limit:
            return reverse_number
        else:
            return 0
    reverse_number = int(str(x)[::-1])
    if reverse_number & pos_limit == reverse_number:
        return reverse_number
    else:
        return 0


# print(reverse(0, 123))
# print(reverse(0, -123))
print(reverse(0, 120))
