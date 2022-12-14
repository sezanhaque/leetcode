class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for row in image:
            for col in range((len(row) + 1) >> 1):
                row[col], row[~col] = row[~col] ^ 1, row[col] ^ 1

        return image


print(Solution.flipAndInvertImage(0, [[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
