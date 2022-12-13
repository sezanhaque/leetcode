# ___________________ Bit Manipulation ___________________


def leftShift(a: int, b: int) -> int:
    """
    Left shift will shift every binary digits to left.
        Ex: 1010 << 1 = 10100
        Here 1010 = 10 (from binary to decimal)
        And 10100 = 20

    So, Left shift will double the power.
        a << b = a * 2^b

    So, 2 << 1 = 2 * 2^1 = 2 * 2  = 4
        5 << 5 = 5 * 2^4 = 5 * 16 = 80
    """
    return a << b


print("*" * 20 + "Left Shift" + "*" * 20)
print(leftShift(2, 3))
print("*" * 20 + "Left Shift" + "*" * 20 + "\n")


def rightShift(a: int, b: int) -> int:
    """
    Right shift will shift every binary digits to Right.
        Ex: 1010 >> 1 = 101
        Here 1010 = 10 (from binary to decimal)
        And 101 = 5

    So, Right shift will divide.
        a >> b = a // 2^b

    So, 2 >> 1 = 2 // 2^1 = 2 // 2  = 1
        8 >> 2 = 8 // 2^2 = 8 // 4 = 2
    """
    return a >> b


print("*" * 20 + "Right Shift" + "*" * 20)
print(rightShift(8, 2))
print("*" * 20 + "Right Shift" + "*" * 20 + "\n")


def bitwiseNot(num: int) -> int:
    """
    Bitwise Not (~) will inverse Binary 0 into 1 and 1 into 0

    It is useful for traversing an array from last index to first index
    If num = 2 then ~num = -3
    """
    arr = [1, 2, 3, 4, 5, 6]

    for i in range(len(arr)):
        print(arr[~i])

    return ~num


print("*" * 20 + "Bitwise Not" + "*" * 20)
print(bitwiseNot(2))
print("*" * 20 + "Bitwise Not" + "*" * 20 + "\n")

# ___________________ Bit Manipulation ___________________


# ___________________ Conversion ___________________


def intToBaseConverter(num: int, base: int) -> str:
    """
    Convert base 10 int to any defined base
    """
    result = ""
    while num != 0:
        num, reminder = divmod(num, base)
        result += str(reminder)
    return result[::-1]


print("*" * 20 + "Int to Base Conversion" + "*" * 20)
print(intToBaseConverter(34, 2))
print("*" * 20 + "Int to Base Conversion" + "*" * 20 + "\n")


def binaryToDecimalConverter(num: str) -> int:
    """
    Convert Binary string to decimal integer
    """

    decimal = 0
    for i in num:
        decimal = (decimal << 1) | int(i)
    return decimal


print("*" * 20 + "Binary to Decimal Conversion" + "*" * 20)
print(binaryToDecimalConverter("100010"))
print("*" * 20 + "Binary to Decimal Conversion" + "*" * 20 + "\n")


def binaryToBaseConverter(num: str, base: int) -> str:
    """
    Convert Binary string to any defined base
    """

    return intToBaseConverter(binaryToDecimalConverter(num), base)


print("*" * 20 + "Binary to Base Conversion" + "*" * 20)
print(binaryToBaseConverter("100010", 8))
print("*" * 20 + "Binary to Base Conversion" + "*" * 20 + "\n")

# ___________________ Conversion ___________________
