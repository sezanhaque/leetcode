def convertToBase7(self, num: int) -> str:
    if not num:
        return "0"
    minus_sign = "-" if num < 0 else ""
    num = abs(num)
    reminder = ""
    while num > 0:
        reminder = str(num % 7) + reminder
        num //= 7
    return minus_sign + reminder


print(convertToBase7(0, 0))  # "0"
print(convertToBase7(0, 100))  # "202"
print(convertToBase7(0, -7))  # "-10"
