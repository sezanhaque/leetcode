def plusOne(self, digits: list[int]) -> list[int]:
    digits[-1] += 1
    for i in range(len(digits) - 1, 0, -1):
        if digits[i] != 10:
            break
        digits[i] = 0
        digits[i - 1] += 1
    if digits[0] == 10:
        digits[0] = 1
        digits.append(0)
    return digits


""" Converting the list to string and then convert it to INT then add 1 then convert it to list again """


def plusOneString(self, digits: list[int]) -> list[int]:
    string = ""
    for i in range(len(digits)):
        string += str(digits[i])

    return [int(c) for c in str(int(string) + 1)]


print(plusOne(0, [9, 9, 9, 9, 9, 9]))
print(plusOneString(0, [9, 9, 9, 9, 9, 9]))
