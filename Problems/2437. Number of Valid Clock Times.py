import re


class Solution:
    def countTime(self, time: str) -> int:
        timeList = []
        for i in range(24):
            for j in range(60):
                timeList.append("%02d:%02d" % (i, j))
        ans = 0
        for s in timeList:
            for i in range(5):
                if time[i] != "?" and time[i] != s[i]:
                    break
            else:
                ans += 1
        return ans

    def countTime(self, time: str) -> int:
        ans = 1

        # for hour first index
        if time[0] == "?":
            # if hour second index
            if time[1] == "?":
                # we know we will get 24 times (0 to 23) value of counter
                ans *= 24
            elif time[1] < "4":
                # if hour second index is less than 4
                # then we can say we have only 3 options (0th, 10th, 20th) for hour first index
                # so we multiply by 3
                ans *= 3
            else:
                # else we have only 2 options (10th, 20th)
                # so we multiply by 2
                ans *= 2

        # for hour second index
        if time[1] == "?":
            # check if hour first digit is in 20th place
            if time[0] == "2":
                # if so then multiply with 4 (24 - 20 = 4)
                ans *= 4
            elif time[0] < "2":
                # if this is less than 2 then we have only 1 hour
                # so for 1 hour we have (0 to 9) = 10 times
                ans *= 10

        # for minute 1st index
        if time[3] == "?":
            # if the first index of minute is missing then we have only (0th to 60th) option => 6 times
            # so we multiply by 6
            ans *= 6

        # for minute 2nd index
        if time[4] == "?":
            # if the second index of minute is missing then we have only (0 to 9) option => 10 times
            # so we multiply by 10
            ans *= 10
        return ans

    # def countTime(self, time: str) -> int:
    #     pattern = time.replace("?", ".")
    #     return sum(
    #         re.fullmatch(pattern, f"{hour:02}:{minute:02}") is not None
    #         for hour in range(24)
    #         for minute in range(60)
    #     )


print(Solution.countTime(0, "1?:00"))
