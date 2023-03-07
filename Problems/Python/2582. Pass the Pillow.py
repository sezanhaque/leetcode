class Solution:
    """
    Going forward and back to the original position, takes n * 2 - 2 steps.

    One loop take n * 2 - 2 steps, so we can first do time %= (n * 2 - 2) to save the time.

    Now we are still at position 1, and it takes n - 1 steps from 1 to n.

    If times < n - 1, not reach n yet.
    If times > n - 1, will go back from n.

    We calculate the distance from n, which abs(n - 1 - time), and return n - abs(n - 1 - time).
    """

    def passThePillow(self, n: int, time: int) -> int:
        return n - abs(n - 1 - time % (n * 2 - 2))


obj = Solution()
print(obj.passThePillow(n=4, time=5))
print(obj.passThePillow(n=3, time=2))
