from functools import cache
from typing import List


class Solution:
    """
    Approach:

        1.  Create an empty set 'wordSet' to store all the words in the given array of strings.

        2.  Create an empty list 'res' to store all the concatenated words.

        3.  Iterate through the array of strings again, for each word, check if it is a concatenated
            word using the function 'DFS(word)'.

        4.  In the 'DFS(word)' function, use a for loop to iterate through each substring of the word,
            starting from index 1 to the second last index of the word.

        5.  For each substring, check if the prefix and suffix of the substring exists in the set 'wordSet'.

        6.  If the prefix and suffix both exist in the set 'wordSet', then return true,
            indicating that the word is a concatenated word.

        7.  If the function 'DFS(word)' returns true, then insert the word into the 'res' list.

        8.  Return the 'res' list.

    Time Complexity and Space Complexity:
        Time complexity:    O(n^2*m) where n is the number of words in the input array
                            and m is the average length of the words.

        The DFS() function is called for each word in the input array, and for each call,
        it iterates through the word to check for possible concatenation, which takes O(m) time.
        The find() function of the set data structure takes O(log(n)) time on average. So, the
        total time complexity of the DFS() function is O(nmlog(n)). Since this function is called
        for each word in the input array, the total time complexity of the findAllConcatenatedWordsInADict()
        function is O(n^2mlog(n)).

        Space complexity:   O(n*m) where n is the number of words in the input array and m is the average
                            length of the words.

        The space complexity O(nm), where n is the number of words in the input array and m is the average
        length of the words.

        The set data structure is used to store all the words in the input array, which takes O(nm) space.
    """

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []

        # create a set from words so we can iterate fast
        words_set = frozenset(words)

        @cache
        def DFS(word: str):
            # iterating from idx 1 because we don't
            # want to prefix an empty string
            for idx in range(1, len(word)):
                prefix = word[:idx]
                suffix = word[idx:]

                # if prefix is in words_set it means suffix might be in the set
                # therefore, we check if suffix in words_set and if not then
                # check every char of suffix via DFS
                if prefix in words_set and (suffix in words_set or DFS(suffix)):
                    return True

            return False

        for word in words:
            if DFS(word):
                res.append(word)

        return res


obj = Solution()
print(obj.findAllConcatenatedWordsInADict(
    ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]))
