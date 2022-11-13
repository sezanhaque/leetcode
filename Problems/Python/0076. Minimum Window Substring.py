from collections import Counter, defaultdict
from math import inf


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        The current window is s[i:j] and the result window is s[I:J].
        In need[c] I store how many times I need character c (can be negative)
        and missing tells how many characters are still missing. In the loop,
        first add the new character to the window. Then, if nothing is missing,
        remove as much as possible from the window start and then update the result.

        Steps:
        1.  Find the first window that contains all letters in t;
        
        2.  Keep expanding the window to the right by 1 char at a time,
            reducing left side if possible. The best part is to make sure
            that THE ACTIVE WINDOW ALWAYS CONTAINS ALL LETTERS IN t.
            In this case, every time the window is expanded,
            only the new char need to be checked.
        """
        if t == "":
            return ""

        need, missing = Counter(t), len(t)
        i = I = J = 0

        for j, c in enumerate(s, 1):
            # if missing > 0, subtract missing
            missing -= need[c] > 0
            need[c] -= 1

            # if nothing is missing
            # remove as much as possible from
            # the window start and then update the result
            if (not J or s[i] == c) and not missing:
                # remove chars to find the real start
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                # update window
                if not J or j - i <= J - I:
                    I, J = i, j

        return s[I:J]

    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = Counter(t), defaultdict(int)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], inf
        l = 0
        for i, c in enumerate(s):
            window[c] += 1

            if c in countT and window[c] == countT[c]:
                have += 1

            # While we have everything we need
            while have == need:
                # update our result
                if (i - l + 1) < resLen:
                    res = [l, i]
                    resLen = i - l + 1
                # pop from the left of our window
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, i = res

        return s[l : i + 1] if resLen != inf else ""


print(Solution.minWindow(0, s="ADOBECODEBANC", t="ABC"))
print(Solution.minWindow(0, s="a", t="a"))
print(Solution.minWindow(0, s="a", t="aa"))
