import math


def print_n_to_one(n: int) -> None:
    """
    Print from n to 1
    """
    if n == 0:
        return
    print(n, end=" ")
    print_n_to_one(n - 1)


# print(print_n_to_one(5))


def print_one_to_n(n: int) -> None:
    """
    Print from 1 to n
    """
    if n == 0:
        return
    print_one_to_n(n - 1)
    print(n, end=" ")


# print(print_one_to_n(5))


def product_of_n_nums(n: int) -> int:
    """
    Product of n to 1 nums
    """
    if n == 1:
        return 1

    return n * product_of_n_nums(n - 1)


# print(product_of_n_nums(5))


def sum_of_digits(n: int) -> int:
    """
    Get the sum of digits of a number
    """
    if n % 10 == n:
        return n
    n, reminder = divmod(n, 10)

    return reminder + sum_of_digits(n)


# print(sum_of_digits(505))


def reverseNumber(n: int) -> int:
    """
    Reverse a number.
    Ex: 123 -> 321

    1. Get total digits: Log 10 base of number + 1
    2. multiply it with 10^(totalDigit - 1)
    3. multiply it with reminder and add remaining number by recursion
    """
    if n % 10 == n:
        return n

    totalDigit = int(math.log10(n)) + 1
    n, reminder = divmod(n, 10)

    return reminder * (10 ** (totalDigit - 1)) + reverseNumber(n)


# print(reverseNumber(1205))


def palindromeNumber(n: int) -> bool:
    """
    Check if a number is palindrome or not.

    Palindrome number: if we reverse a number, it will be the same as the original number.

    Ex: 12321 -> palindrome
        12354 -> not palindrome
    """
    return n == reverseNumber(n)


# print(palindromeNumber(12321))


def countZeros(n: int, count: int = 0) -> int:
    """
    Count the number of zeros of a number.

    Ex: 1203506 -> number of zeros will be 2
    """
    if n % 10 == n:
        return count

    n, reminder = divmod(n, 10)

    if reminder == 0:
        return countZeros(n, count + 1)
    else:
        return countZeros(n, count)


# print(countZeros(1203506))


def sortedArray(arr: list[int], idx: int = 0) -> bool:
    """
    Check if the array is sorted in ascending order.
    """
    if idx == len(arr) - 1:
        return True

    return arr[idx] <= arr[idx + 1] and sortedArray(arr, idx + 1)


# print(sortedArray([1, 2, 3, 2]))


def trianglePattern(n: int) -> None:
    if n == 0:
        return

    print("*" * n)
    return trianglePattern(n - 1)


print(trianglePattern(5))
