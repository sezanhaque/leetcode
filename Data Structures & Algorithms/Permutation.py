from functools import cache
from itertools import permutations


class Permutation:
    """
    Create permutation from a string and store them in an array.

    Solution:

        1.  Loop through the length of output string + 1.

        2.  We will recursively call the generate function
            to shuffle every first char of input string.

            We will make the output string as follows:
            *   Start = 0 - ith index of output string
            *   1st char of input index
            *   End = ith - last index of output string

            And input string as from 1st index to last.
    """

    def __init__(self, s: str) -> None:
        self.ans = []
        self.s = s

    def get(self) -> list[str]:
        self.generate(self.s, "")
        return self.ans

    @cache
    def generate(self, input: str, output: str) -> None:
        if len(input) == 0:
            self.ans.append(output)
            return

        # Iterate over output string inclusive its length
        # This way we will always take the first char of input
        for i in range(len(output) + 1):
            # 0th to ith index of output
            start = output[0:i]

            # ith to last index of output
            end = output[i:]

            # 1st char of input
            char = input[0]

            # and make the input string from 1st to last index
            self.generate(input[1:], start + input[0] + end)

    def usingItertools(self) -> list[str]:
        # Get permutation using itertools
        return ["".join(p) for p in permutations(self.s)]


obj = Permutation("abc")
print(obj.get())
print(obj.usingItertools())
