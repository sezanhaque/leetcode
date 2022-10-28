import collections
import re


def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
    banned = set(banned)  # set is faster than list
    words = re.findall(r"[a-zA-z]+", paragraph.lower())
    count = collections.Counter(words)
    for word in words:
        if word in banned:
            count[word] = 0
    return count.most_common(1)[0][0]


print(
    mostCommonWord(
        0, "Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]
    )
)  # "ball"
