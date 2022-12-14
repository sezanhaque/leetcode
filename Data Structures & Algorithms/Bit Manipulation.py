# ___________________ Bit Manipulation ___________________


import math


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
print("*" * 20 + "Left Shift" + "*" * 20 + "\n\n")


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
print("*" * 20 + "Right Shift" + "*" * 20 + "\n\n")


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
print("*" * 20 + "Bitwise Not" + "*" * 20 + "\n\n")


def isEven(num: int) -> bool:
    """
    We can easily check if the number is even or odd
    by using & operator.

    If we "& any number by 1" it will return 0 (for even) or 1 (for odd)

    Let 2 = 10
      & 1 = 01
    ___________________
      ans = 00

    If the number is even then it will always return 0
    If the number is odd then it will always return 1

    *** Using this method we can always get the last binary digit of a number ***
    """
    return not num & 1


print("*" * 20 + "Even & Odd using & operator" + "*" * 20)
print(isEven(3))
print("*" * 20 + "Even & Odd using & operator" + "*" * 20 + "\n\n")


def magicNumber(num: int) -> int:
    """
    *** Amazon question ***

    Represent the num into binary number
    Then from the last digit, multiply that digit
    with 5^idx and add it to the result.

    Ex: num = 5 = 101
    from last digit => 1 * 5^1 + 0 * 5^2 + 1 * 5^3 = 5 + 0 + 125 = 130

    So, 5th magic number is 125.
    """
    res, base = 0, 5

    while num > 0:
        # get the last binary digit using &
        last = num & 1

        # Right shift the num so that we can get next last digit
        num = num >> 1

        res += last * base
        base *= 5

    return res


print("*" * 20 + "Magic Number" + "*" * 20)
print(magicNumber(3))
print("*" * 20 + "Magic Number" + "*" * 20 + "\n\n")


def numberOfDigits(num: int, base: int) -> int:
    """
    Get the number of digits of any base number

    Ex:
        10 in decimal (base 10) => 2 digits
        10 in binary (base 2) => 1010 => 4 digits

    Formula:
        Number of digits = log base num + 1
                         = log(num) // log(base) + 1
    """
    return math.log(num) // math.log(base) + 1


print("*" * 20 + "Number of digits of a number" + "*" * 20)
print(numberOfDigits(10, 10))
print("*" * 20 + "Number of digits of a number" + "*" * 20 + "\n\n")


def sum_of_row_in_pascal_triangle(row: int) -> int:
    """
    For nth row, sum = 2^(n-1)
    """
    return 1 << (row - 1)


print("*" * 20 + "Sum of row in a Pascal's triangle" + "*" * 20)
print(sum_of_row_in_pascal_triangle(5))
print("*" * 20 + "Sum of row in a Pascal's triangle" + "*" * 20 + "\n\n")


def power_of_two(num: int) -> bool:
    """
    Check if the number if power of 2

    Power of 2 will have only one 1

    Ex: 4 = 100, 8 = 1000

    If we can check if there is only one 1
    then we can decide if this is power of 2

    We can & every binary digit with its opposite
    and if the ans is 0 then we get the power of 2.

    Ex:
    4         = 100,
    4 - 1 = 3 = 011
            & = 000 power of 2


    5         = 101,
    5 - 1 = 4 = 100
            & = 100 not power of 2

    Formula: num & num - 1 == 0 ? True : False
    """
    return not num & (num - 1)


print("*" * 20 + "Power of 2" + "*" * 20)
print(power_of_two(4))
print("*" * 20 + "Power of 2" + "*" * 20 + "\n\n")


def pow(num: int, power: int) -> int:
    """
    Math power function
    returns num^power
    """
    res = 1
    while power > 0:
        if power & 1:
            res *= num
        num *= num
        power >>= 1
    return res


print("*" * 20 + "Math Pow function" + "*" * 20)
print(pow(3, 6))
print("*" * 20 + "Math Pow function" + "*" * 20 + "\n\n")


def num_of_set_bits(num: int) -> int:
    """
    Get the number of set bits of a number.

    Set bits are number of 1 in a binary number.
    """
    count = 0
    while num > 0:
        num = num & (num - 1)
        count += 1
    return count


print("*" * 20 + "Number of set bits" + "*" * 20)
print(num_of_set_bits(45))  # 45 = 101101
print("*" * 20 + "Number of set bits" + "*" * 20 + "\n\n")


def rangeXOR(a: int, b: int) -> int:
    """
    Range XOR for a to b = xor(b) ^ xor(a-1)
    """
    return xor(b) ^ xor(a - 1)


def xor(a: int) -> int:
    if a % 4 == 0:
        return a
    if a % 4 == 1:
        return 1
    if a % 4 == 2:
        return a + 1
    return 0


print("*" * 20 + "XOR" + "*" * 20)
print(rangeXOR(3, 9))
print("*" * 20 + "XOR" + "*" * 20 + "\n\n")


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
print("*" * 20 + "Int to Base Conversion" + "*" * 20 + "\n\n")


def binaryToDecimalConverter(num: str) -> int:
    """
    Convert Binary string to decimal integer
    """

    decimal = 0
    for i in num:
        decimal = (decimal << 1) | int(i)
    return decimal


print("*" * 20 + "Binary to Decimal Conversion" + "*" * 20)
print(binaryToDecimalConverter("101"))
print("*" * 20 + "Binary to Decimal Conversion" + "*" * 20 + "\n\n")


def binaryToBaseConverter(num: str, base: int) -> str:
    """
    Convert Binary string to any defined base
    """

    return intToBaseConverter(binaryToDecimalConverter(num), base)


print("*" * 20 + "Binary to Base Conversion" + "*" * 20)
print(binaryToBaseConverter("100010", 8))
print("*" * 20 + "Binary to Base Conversion" + "*" * 20 + "\n\n")

# ___________________ Conversion ___________________
