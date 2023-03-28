from collections import deque
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        passes = 3
        ticket_days = [1, 7, 30]
        cost = 0

        queues = [deque() for _ in range(passes)]

        for day in days:
            for ticket in range(passes):
                # while current day is greater than first value day of queue
                # we pop it out from the queue
                while queues[ticket] and queues[ticket][0][0] + ticket_days[ticket] <= day:
                    queues[ticket].popleft()

                # We keep pairs [day, cost]
                queues[ticket].append([day, cost + costs[ticket]])

            cost = min(queues[idx][0][1] for idx in range(passes))

        return cost


obj = Solution()
print(obj.mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]))
