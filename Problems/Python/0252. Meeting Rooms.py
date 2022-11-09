class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    # Premium

    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])

        for idx in range(len(intervals) - 1):
            if intervals[idx][1] > intervals[idx + 1][0]:
                return False

        return True


print(Solution.canAttendMeetings(0, [[0, 30], [5, 10], [15, 20]]))  # False
print(Solution.canAttendMeetings(0, [[7, 10], [2, 4]])) # True
