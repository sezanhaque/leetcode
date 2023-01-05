from collections import deque
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # creating a pair of position and speed
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = deque()

        # traversing in reverse order of sorted pair
        for p, s in sorted(pair)[::-1]:
            # calculating time needed to reach target
            # and append it to stack
            stack.append((target - p) / s)

            # if len of stack >=2, it means we can
            # compare between 2 cars.
            # so we are checking if the time of top car
            # is less than the second one then both of them
            # will become 1 car fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [(target - p) / s for p, s in sorted(zip(position, speed))]
        res = curr = 0

        for t in time[::-1]:
            if t > curr:
                res += 1
                curr = t

        return res

obj = Solution()
print(obj.carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))
