class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        aSum = bSum = i = 0
        vowels = set("aeiou")
        for i in range(n >> 1):
            if s[i].lower() in vowels:
                aSum += 1
            if s[n - i - 1].lower() in vowels:
                bSum += 1

        return aSum == bSum

    def halvesAreAlike(self, s: str) -> bool:
        n, vowels = len(s), set("aeiou")
        return sum(i.lower() in vowels for i in s[: n >> 1]) == sum(
            i.lower() in vowels for i in s[n >> 1 :]
        )


print(Solution.halvesAreAlike(0, "book"))
print(Solution.halvesAreAlike(0, "textbook"))
print(Solution.halvesAreAlike(0, "AbCdEfGh"))
