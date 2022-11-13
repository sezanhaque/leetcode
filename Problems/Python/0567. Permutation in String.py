from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        length = len(s1)
        s1Counter = Counter(s1)

        for idx in range(length, len(s2) + 1):
            if Counter(s2[idx - length : idx]) == s1Counter:
                return True

        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        The only thing we care about any particular substring in s2
        is having the same number of characters as in the s1.
        So we create a hashmap with the count of every character in the string s1.
        Then we slide a window over the string s2 and decrease the counter for
        characters that occurred in the window. As soon as all counters in the
        hashmap get to zero that means we encountered the permutation.
        """
        s1Counter, length = Counter(s1), len(s1)

        for i in range(len(s2)):
            if s2[i] in s1Counter:
                s1Counter[s2[i]] -= 1

            if i >= length and s2[i - length] in s1Counter:
                s1Counter[s2[i - length]] += 1

            if all(s1Counter[i] == 0 for i in s1Counter):
                return True

        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        We can use an auxiliary variable to count a number of
        characters whose frequency gets to zero during window sliding.
        That helps us to avoid iterating over the hashmap for every
        cycle tick to check whether frequencies turned into zero.

        # Optimized
        """
        s1Counter, length, match = Counter(s1), len(s1), 0

        for i in range(len(s2)):
            if s2[i] in s1Counter:
                s1Counter[s2[i]] -= 1
                if not s1Counter[s2[i]]:
                    # if counter == 0 then increment the match
                    # because it means we have found the total
                    # number of char in s2
                    match += 1

            if i >= length and s2[i - length] in s1Counter:
                # checking of the beginning letter inside the current sliding window
                if not s1Counter[s2[i - length]]:
                    # if counter == 0 then decrement the match
                    # because it means we have found misplaced the total
                    # number of char in s2
                    match -= 1

                s1Counter[s2[i - length]] += 1

            if match == len(s1Counter):
                return True

        return False


# print(Solution.checkInclusion(0, s1="ab", s2="eidbaooo"))
print(Solution.checkInclusion(0, s1="ab", s2="eidboaoo"))
