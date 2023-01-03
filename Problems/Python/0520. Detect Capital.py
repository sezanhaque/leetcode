class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # every char should be upper
        if word.isupper():
            return True

        # first char upper
        # rest will be lower
        elif word[0].isupper():
            for idx in range(1, len(word)):
                if word[idx].isupper():
                    return False
            return True

        # every char should be lower
        else:
            for w in word:
                if w.isupper():
                    return False
            return True

    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()

    def detectCapitalUse(self, word: str) -> bool:
        """
        Let us evaluate number of capital letters first:

        If number of capital letters is equal to 0, then we return True.
        If number of capital letters is equal to n - number of all letters, we also return True.
        If number of capital letters is equal to 1 and first letter is capital, we return True.
        If none of 3 conditions above fulfilled, we return False.
        """
        Num_cap, n = 0, len(word)

        for letter in word:
            Num_cap += letter.isupper()

        if Num_cap == 0 or Num_cap == n or Num_cap == 1 and word[0].isupper():
            return True

        return False


obj = Solution()
print(obj.detectCapitalUse("USA"))
# print(obj.detectCapitalUse("Google"))
# print(obj.detectCapitalUse("FlaG"))
# print(obj.detectCapitalUse("g"))
