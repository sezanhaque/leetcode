def findContentChildren(self, g: list[int], s: list[int]) -> int:
    g, s = sorted(g), sorted(s)

    cookies, child = 0, 0

    while cookies < len(s) and child < len(g):
        if s[cookies] >= g[child]:
            child += 1
        cookies += 1

    return child


print(findContentChildren(0, [1, 2, 3], [1, 1]))
print(findContentChildren(0, [1, 2], [1, 2, 3]))
