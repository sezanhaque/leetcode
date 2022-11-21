class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Let us assume we are in the ground floor
        and our initial step is 1
        So every time we take one step to climb the staircase
        """
        step, climb = 1, 0

        for i in range(1, n + 1):
            step, climb = step + climb, step

        return step


print(Solution.climbStairs(0, 3))
