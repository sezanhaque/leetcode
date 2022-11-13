class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    # Premium

    def encode(self, strs: list[str]) -> str:
        """
        Encode string from "leet" to "4#leet"
        4 is the length of the string
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """

    def decode(self, str: str) -> list[str]:
        res, i = [], 0

        while i < len(str):
            j = i

            while str[j] != "#":
                j += 1

            length = int(str[i:j])
            res.append(str[j + 1 : j + length + 1])
            i = j + length + 1

        return res


if __name__ == "__main__":
    encodedStr = Solution.encode(0, ["lint", "code", "love", "you"])
    decodedStr = Solution.decode(0, encodedStr)

    print(encodedStr, decodedStr)
