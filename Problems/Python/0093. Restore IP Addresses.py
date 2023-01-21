from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        # to make a valid IP address we have max 4 parts with 3 numbers
        # so length must be between 4 * 3 = 12
        if len(s) > 12:
            return res

        def isValid(temp: str) -> bool:
            # if len is greater than 3 then we have crossed
            # max char of a part of an IP address
            # or if len is 0 then there is no str
            if len(temp) > 3 or len(temp) == 0:
                return False

            # if len > 1, we need to check if there is any
            # leading 0 or not
            if len(temp) > 1 and temp[0] == '0':
                return False

            # we need to check if the num is between 0 - 255
            if len(temp) and int(temp) > 255:
                return False

            return True

        def solve(idx: int, currStr: str, dots: int):
            # if there are 3 dots "." it means
            # we have a figure to check if it is a valid
            # IP address or not, so we will check its validity
            if dots == 3:
                if isValid(s[idx:]):
                    res.append(currStr + s[idx:])
                return

            # we will iterate from idx to idx + 3 / len(s)
            # which one is minimum
            for j in range(idx, min(idx + 3, len(s))):
                if isValid(s[idx:j + 1]):
                    new_currStr = currStr + s[idx: j + 1] + '.'
                    solve(j + 1, new_currStr, dots + 1)

        solve(0, "", 0)
        return res


obj = Solution()
print(obj.restoreIpAddresses("25525511135"))
