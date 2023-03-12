from typing import List


class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks = sorted(tasks, key=lambda x: x[1])
        chosen_set = set()

        for start, end, duration in tasks:
            for time in chosen_set:
                # if current time is in between start and end
                # subtract the duration
                if start <= time <= end:
                    duration -= 1

                if not duration:
                    break

            while duration > 0:
                if end not in chosen_set:
                    chosen_set.add(end)
                    duration -= 1
                end -= 1

        return len(chosen_set)


obj = Solution()
print(obj.findMinimumTime([[2, 3, 1], [4, 5, 1], [1, 5, 2]]))
