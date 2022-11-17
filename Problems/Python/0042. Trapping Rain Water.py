from collections import deque


class Solution:
    def trap(self, height: list[int]) -> int:
        # Two Pointer Approach

        """
        Intuition

        *   Keep track of the already safe level and the total water so far.
        *   In each step, process and discard the lower one of the leftmost or rightmost elevation.

        Max Level       :   Tracks the Max Level which water will not stay above this but stay below this.
                            So if lower is less than Max Level we will have water accumulation.

        Current Lower   :   This is the floor of the moment. Moment basically is either left side or right side.
                            We are either looking at the left pointer or right pointer. Whichever is lower.

        Algorithm

        *   Initialize left pointer to 0 and right pointer to len - 1
        *   Initialize leftMax to left and rightMax to right index

        *   While left < right:
                *   If height[left] is smaller than height[right]
                        *   Assign current value height[left] to currLevel
                        *   Update left to left + 1
                *   Else
                        *   Assign current value height[right] to currLevel
                        *   Update right to right - 1
                *   Get max between maxLevel and currLevel
                *   Add difference between maxLevel and currLevel (this is where water will be trapped) to water

        Time complexity     : O(n)
        Space complexity    : O(1)
        """

        left, right = 0, len(height) - 1
        maxLevel = water = 0

        while left < right:
            if height[left] < height[right]:
                currLevel = height[left]
                left += 1
            else:
                currLevel = height[right]
                right -= 1
            maxLevel = max(maxLevel, currLevel)
            water += maxLevel - currLevel

        return water


print(Solution.trap(0, [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(Solution.trap(0, [4, 2, 0, 3, 2, 5]))
