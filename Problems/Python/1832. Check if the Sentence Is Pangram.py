from collections import Counter


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        sentence_counter = Counter(sentence)

        for char in alphabets:
            if sentence_counter[char] < 1:
                return False

        return True

    def checkIfPangram(self, sentence: str) -> bool:
        return True if len(set(sentence)) == 26 else False


obj = Solution()
print(obj.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(obj.checkIfPangram("leetcode"))
