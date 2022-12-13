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

    def climbStairs(self, n: int) -> int:
        memo ={}
        memo[1] = 1
        memo[2] = 2
        
        def climb(n):
            # if the recurssion already done before first take a look-up in the look-up table
            if n in memo: 
                return memo[n]
            # Store the recurssion function in the look-up table and reuturn the stored look-up table function
            else:   
                memo[n] =  climb(n-1) + climb(n-2)
                return memo[n]
        
        return climb(n)


print(Solution.climbStairs(0, 3))
