import heapq
from collections import namedtuple
from typing import List, Tuple


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        Task = namedtuple("Task", ['e_time', 'p_time', 'idx'])

        # Sort the tasks by enqueue time, the shortest processing time and index
        sorted_task = sorted([Task(task[0], task[1], idx) for idx, task in enumerate(tasks)])

        heap: List[Tuple[int, int]] = []
        res: List[int] = []

        # idx: current task index
        # time: current CPU clock
        idx = time = 0

        while len(res) < len(tasks):
            # Push all the tasks available at current CPU clock time
            while idx < len(tasks) and sorted_task[idx].e_time <= time:
                # store to heap: processing time, index
                # whose enqueue time <= current time
                heapq.heappush(heap, (sorted_task[idx].p_time, sorted_task[idx].idx))
                idx += 1

            # we have to complete the tasks those are in heap
            if heap:
                p_time, index = heapq.heappop(heap)

                # Tasks in heap will increase the current time
                # So we are adding their processing time with time
                time += p_time

                # And lastly we are adding the index of the task to res
                res.append(index)

            # If heap is empty, it means CPU is idle
            # so go to the next task
            else:
                time = sorted_task[idx].e_time

        return res


obj = Solution()
print(obj.getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]))
