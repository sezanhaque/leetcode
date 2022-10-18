def countOdds(self, low: int, high: int) -> int:
    if low % 2 == 0 and high % 2 == 0:
        return (high - low) // 2
    else:
        return (high - low) // 2 + 1


def countOdds(self, low: int, high: int) -> int:
    return (high + 1) // 2 - low // 2


print(countOdds(0, 3, 7))  # Odd, Odd 3
print(countOdds(0, 8, 10))  # Even, Even 1

print(countOdds(0, 1, 10))  # Odd, Even 5
print(countOdds(0, 0, 11))  # Even, Odd 6

print(countOdds(0, 1, 11))  # Odd, Odd 6
print(countOdds(0, 0, 10))  # Even, Even 5
