"""
Input: s = "0110101"
Output: 4
Explanation: 
After one second, s becomes "1011010".
After another second, s becomes "1101100".
After the third second, s becomes "1110100".
After the fourth second, s becomes "1111000".
No occurrence of "01" exists any longer, and the process needed 4 seconds to complete,
so we return 4.

Input: s = "11100"
Output: 0
Explanation:
No occurrence of "01" exists in s, and the processes needed 0 seconds to complete,
so we return 0.
"""


def secondsToRemoveOccurrences(self, s: str) -> int:
    count = 0
    temp = ""
    ones = s.count("1")  # get the count of 1
    for _ in range(ones):
        # make a string with total number of 1
        temp += "1"

    while s[:ones] != temp:
        # loop through index 0 to count of 1 while the string is not equal to temp string
        left, right = 0, 1
        while right < len(s):
            """
            Compare the two index from left to right if
            they both are equal to "01"
            if so then replace them
            """
            if s[left : left + 1] + s[right : right + 1] == "01":
                s = s.replace(s[left : left + 1] + s[right : right + 1], "10")
                count += 1
            left += 1
            right += 1
    return count


def secondsToRemoveOccurrences(self, s: str) -> int:
    count = 0
    while "01" in s:
        """
        While we are getting "01" in the string
        we will replace them into "10"
        and count the number of occurrence
        """
        s = s.replace("01", "10")
        count += 1
    return count


print(secondsToRemoveOccurrences(0, "0110101"))
# print(secondsToRemoveOccurrences(0, "11100"))
# print(secondsToRemoveOccurrences(0, "001011"))
# print(secondsToRemoveOccurrences(0, "1101"))
