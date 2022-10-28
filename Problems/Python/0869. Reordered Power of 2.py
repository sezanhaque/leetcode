def reorderedPowerOf2(self, n: int) -> bool:
    sorted_str = sorted([int(x) for x in str(n)])

    for i in range(30):
        towPower = sorted([int(x) for x in str(1 << i)])
        if towPower == sorted_str:
            return True
        if len(towPower) > len(sorted_str):
            return False
    return False


print(reorderedPowerOf2(0, 4))
print(reorderedPowerOf2(0, 10))
