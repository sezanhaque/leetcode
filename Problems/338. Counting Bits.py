def countBits(self, n: int) -> list[int]:
    result = []
    for i in range(n + 1):
        result.append(intToBinary(0, i).count("1"))
    return result


def countBits(self, n: int) -> list[int]:
    counter = [0]
    for i in range(1, n + 1):
        print(counter[i >> 1], i % 2, counter[i >> 1] + i % 2)
        counter.append(counter[i >> 1] + i % 2)
    return counter


def intToBinary(self, n: int) -> str:
    binary_string = ""
    while n > 0:
        n, digit = divmod(n, 2)
        binary_string += str(digit)
    return binary_string[::-1]


print(countBits(0, 5))
