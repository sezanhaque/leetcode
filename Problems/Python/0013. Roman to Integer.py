from operator import index


def romanToInt(self, s: str) -> int:
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    index_value = list(roman.keys())
    sum = 0
    idx = len(s) - 1
    while idx > -1:
        if idx == len(s) - 1:
            sum = sum + roman.get(s[idx])
        else:
            if index_value.index(s[idx]) < index_value.index(s[idx + 1]):
                sum = sum - roman.get(s[idx])
            else:
                sum = sum + roman.get(s[idx])
        idx -= 1
    return sum


def romanToInt(self, s: str) -> int:
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result, previous_number = 0, 0

    for symbol in s[::-1]:
        if roman[symbol] >= previous_number:
            result += roman[symbol]
        else:
            result -= roman[symbol]
        previous_number = roman[symbol]
    return result


print(romanToInt(0, "MCMXCIV"))
print(romanToInt(0, "LVIII"))
print(romanToInt(0, "III"))
print(romanToInt(0, "IV"))
