def removeAnagrams(self, words: list[str]) -> list[str]:
    """ "1st solution"""
    # for i in range(0, len(words) - 1):
    #     for j in range(i + 1, len(words)):
    #         print("Words: ", words[i], words[i + 1])
    #         if len(words[i]) == len(words[i + 1]):
    #             if sorted(words[i]) == sorted(words[i + 1]):
    #                 print("words i+1: ", words[i + 1])
    #                 # print(words.pop(i + 1))
    #                 words.pop(i + 1)
    # return words

    """"2nd solution"""
    i = 1
    while i < len(words):
        if sorted(words[i]) == sorted(words[i - 1]):
            words.pop(i)
        else:
            i += 1

    return words

    """"3rd solution"""
    # previous_word = ""
    # result = []
    # for word in words:
    #     current_word = sorted(word)
    #     if current_word != previous_word:
    #         result.append(word)
    #     previous_word = current_word
    # return result


print(removeAnagrams(0, ["abba", "baba", "bbaa", "cd", "cd", "abab"]))
print(removeAnagrams(0, ["a", "b", "c", "d", "e"]))
