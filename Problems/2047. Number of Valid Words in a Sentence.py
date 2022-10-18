
import re


def countValidWords(self, sentence: str) -> int:
    words = sentence.split()
    pattern = re.compile(r"^([a-z]+\-?[a-z]+[!\.,]?)$|^([a-z]*[!\.,]?)$")
    count = 0
    for word in words:
        if re.match(pattern, word):
            count += 1
    return count


print(countValidWords(0, "cat and  dog"))
print(countValidWords(0, "!this  1-s b8d!"))
