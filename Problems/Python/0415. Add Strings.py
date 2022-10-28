def addStrings(self, num1: str, num2: str) -> str:
    """Using built-in string and int function"""
    # return str(int(num1) + int(num2))

    """ Using custom function """
    return int_to_string(string_to_int(num1) + string_to_int(num2))


def string_to_int(value: str) -> int:
    """Convert String to Integer"""
    result = 0
    for i in value:
        result = result * 10 + ord(i) - ord("0")

    return result


def int_to_string(i: int) -> str:
    """Convert Integer to String"""
    string = ""
    while True:
        i, remainder = divmod(i, 10)
        string = chr(ord("0") + remainder) + string
        if i == 0:
            break
    return string


print(addStrings(0, "123", "11"))
