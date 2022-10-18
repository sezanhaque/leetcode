def isSameAfterReversals(self, num: int) -> bool:
    reverse_number = int(str(num)[::-1])
    reverse_number = int(str(reverse_number)[::-1])
    return True if num == reverse_number else False


def isSameAfterReversals(self, num: int) -> bool:
    """
    If the number is 0 then true
    If the number is divided by 10 and there is no reminder then it has a 0 at the end of the number. -> False
    Else True
    """
    if num == 0:
        return True
    elif num % 10 == 0:
        return False
    return True


print(isSameAfterReversals(0, 526))
print(isSameAfterReversals(0, 1200))
