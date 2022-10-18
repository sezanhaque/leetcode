from collections import Counter


def countWords(self, words1: list[str], words2: list[str]) -> int:
    count = Counter(words1 + words2)
    return len(
        [
            word
            for word in count
            if count[word] == 2 and word in words1 and word in words2
        ]
    )


print(
    countWords(
        0, ["leetcode", "is", "amazing", "as", "is"], ["amazing", "leetcode", "is"]
    )
)
# print(countWords(0, ["b", "bb", "bbb"], ["a", "aa", "aaa"]))
# print(countWords(0, ["a", "ab"], ["a", "a", "a", "ab"]))
