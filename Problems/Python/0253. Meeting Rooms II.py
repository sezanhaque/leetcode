class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    # Premium

    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        # If there are no meetings, we don't need any rooms.
        if not intervals:
            return 0

        # Separate out the start and the end timings and sort them individually.
        start = sorted((i[0] for i in intervals))
        end = sorted(i[1] for i in intervals)

        # The two pointers in the algorithm: e_ptr and s_ptr.
        start_pointer = end_pointer = used_rooms = 0

        while start_pointer < len(intervals):
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start[start_pointer] >= end[end_pointer]:
                # Free up a room and increment the end_pointer.
                end_pointer += 1
                used_rooms -= 1

            # We do this irrespective of whether a room frees up or not.
            # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
            # remain the same in that case. If no room was free, then this would increase used_rooms
            start_pointer += 1
            used_rooms += 1

        return used_rooms

    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        # NeetCode

        start = sorted((i[0] for i in intervals))
        end = sorted(i[1] for i in intervals)

        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res


print(Solution.minMeetingRooms(0, [[0, 30], [5, 10], [15, 20]]))  # 2
print(Solution.minMeetingRooms(0, [[7, 10], [2, 4]]))  # 1
