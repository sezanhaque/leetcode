def countDaysTogether(
    self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
) -> int:
    def getDate(date):
        monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month = int(date[:2])
        days = int(date[3:])
        print(sum(monthList[: month - 1]) + days)
        return sum(monthList[: month - 1]) + days

    print(min(leaveAlice, leaveBob), max(arriveAlice, arriveBob))
    return max(0, getDate(min(leaveAlice, leaveBob)) - getDate(max(arriveAlice, arriveBob)) + 1)


print(countDaysTogether(0, "08-15", "08-18", "08-16", "08-19"))
# print(countDaysTogether(0, "10-01", "10-31", "11-01", "12-31"))
# print(countDaysTogether(0, "10-20", "12-22", "06-21", "07-05"))
# print(countDaysTogether(0, "09-01", "10-19", "06-19", "10-20"))

# 16627
