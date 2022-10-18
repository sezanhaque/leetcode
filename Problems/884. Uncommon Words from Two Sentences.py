from collections import Counter


def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
    count = Counter((s1 + " " + s2).split())
    return [idx for idx in count if count[idx] == 1]


print(uncommonFromSentences(0, "this apple is sweet", "this apple is sour"))
print(uncommonFromSentences(0, "apple apple", "banana"))
