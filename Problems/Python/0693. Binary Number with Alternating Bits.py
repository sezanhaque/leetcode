def hasAlternatingBits(self, n: int) -> bool:
    bin_value = bin(n)[2:]
    for i in range(len(bin_value) - 1):
        if bin_value[i] == bin_value[i + 1]:
            return False
    return True


print(hasAlternatingBits(0, 5))
print(hasAlternatingBits(0, 7))
print(hasAlternatingBits(0, 12))
print(hasAlternatingBits(0, 10))
