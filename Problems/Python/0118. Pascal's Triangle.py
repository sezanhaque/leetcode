class Solution:
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

    def generate(self, numRows: int) -> list[list[int]]:
        ans = [None] * numRows

        for i in range(numRows):
            ans[i] = [1] * (i + 1)  # row
            for j in range(1, (i >> 1) + 1):
                # from first
                ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]

                # from last
                ans[i][i - j] = ans[i][j]
        return ans


print(Solution.generate(0, 5))
