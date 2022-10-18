def addBinary(self, a: str, b: str) -> str:
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    result = ""
    carry = 0
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == "1" else 0
        r += 1 if b[i] == "1" else 0
        result = ("1" if r % 2 == 1 else "0") + result

        carry = 0 if r < 2 else 1

    if carry != 0:
        result = "1" + result

    print(result.zfill(max_len))
    # return result.zfill(max_len)
    
    """Using built-in function"""
    # return bin(int(a, 2) + int(b, 2))[2:]

addBinary(0, "1010", "1011")
