from re import L


def maxDistance(self, colors: list[int]) -> int:
    max_distance = 0
    for i in range(len(colors)):
        for j in range(len(colors) - 1, 0, -1):
            if colors[i] != colors[j] and j > i:
                max_distance = max(max_distance, j - i)
    return max_distance


print(maxDistance(0, [1, 1, 1, 6, 1, 1, 1, 1, 3]))
print(maxDistance(0, [1, 8, 3, 8, 3]))
print(maxDistance(0, [0, 1]))
print(maxDistance(0, [9, 9, 9, 18, 9, 9, 9, 9, 9, 18]))
print(maxDistance(0, [6, 6, 6, 6, 6, 6, 6, 6, 6, 19, 19, 6, 6]))
print(maxDistance(0, [4,4,4,11,4,4,11,4,4,4,4,4]))
