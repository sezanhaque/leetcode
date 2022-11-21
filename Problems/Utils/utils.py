def intToBaseConverter(num, base):
    """
    Convert base 10 int to any defined base
    """
    result = ""
    while num != 0:
        num, reminder = divmod(num, base)
        result += str(reminder)
    return result[::-1]


print(intToBaseConverter(34, 6))
