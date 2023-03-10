import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.range = []

        while head:
            self.range.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        pick = random.randint(0, len(self.range) - 1)
        return self.range[pick]


class Solution2:
    """
    Reservoir Sampling
    Solution Link: https://leetcode.com/problems/linked-list-random-node/solutions/956872/python-reservoir-sampling-follow-up-explained/
    """

    def __init__(self, head):
        self.head = head

    def getRandom(self):
        n, k = 1, 1
        head, ans = self.head, self.head
        while head.next:
            n += 1
            head = head.next
            if random.random() < k / n:
                ans = ans.next
                k += 1

        return ans.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
