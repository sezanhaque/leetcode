def generate(self, numRows: int) -> list[list[int]]:
    result = []
    for i in range(numRows):
        sub_result = []
        for j in range(i + 1):
            if j == 0 or j == i:
                sub_result.append(1)
            else:
                sub_result.append(result[i - 1][j - 1] + result[i - 1][j])
        result.append(sub_result)
    return result
    
print(generate(0, 5))
