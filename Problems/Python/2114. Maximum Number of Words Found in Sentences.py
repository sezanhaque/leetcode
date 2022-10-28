from unittest import result


def mostWordsFound(self, sentences: list[str]) -> int:
    max_word = 0
    for i in sentences:
        count = i.count(" ") + 1
        if count > max_word:
            max_word = count
    return max_word
    result = max([i.count(" ") + 1 for i in sentences])
    print(result)


print(
    mostWordsFound(
        0,
        [
            "alice and bob love leetcode",
            "i think so too",
            "this is great thanks very much",
        ],
    )
)
