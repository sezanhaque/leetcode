class Solution:
    """
    We have to track every starting and closing bracket.
    And store the max closed brackets.
    Then divide the max by 2.

    Because for 2 misplaced close brackets,
    we need to make only 1 swap.

    Solution:
        
        1.  If the current char is open bracket
            then subtract 1 with close.

            If the current char is closed
            then add 1 with close.

        2.  Update the maxClose.

        3.  Return maxClose + 1 // 2.
            (we are adding 1 for odd number)

    Complexity:
        Time: O(n)
        Space: O(1)
    """

    def minSwaps(self, s: str) -> int:
        close, swap = 0, 0

        for char in s:
            if char == "[":
                close -= 1
            else:
                close += 1
            swap = max(swap, close)

        return (swap + 1) >> 1


print(Solution.minSwaps(0, "][]["))
