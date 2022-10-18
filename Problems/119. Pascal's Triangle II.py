def getRow(self, rowIndex: int) -> list[int]:
    result = []
    for i in range(rowIndex + 1):
        sub_result = []
        for j in range(i + 1):
            if j == 0 or j == i:
                sub_result.append(1)
            else:
                sub_result.append(result[i - 1][j - 1] + result[i - 1][j])
        result.append(sub_result)
    return result[rowIndex]
    
def getRow(self, rowIndex: int) -> list[int]:
    ans = [1]
    for _ in range(rowIndex):
        ans = [sum(val) for val in zip([0] + ans, ans + [0])]
    return ans

print(getRow(0, 3))
