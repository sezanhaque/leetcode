import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or not len(lists):
            return None

        while len(lists) > 1:
            mergedLists = []

            for idx in range(0, len(lists), 2):
                list1 = lists[idx]
                list2 = lists[idx + 1] if (idx + 1) < len(lists) else None

                mergedLists.append(self.mergeTwoLists(list1, list2))

            lists = mergedLists

        return lists[0]

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # LeetCode Problem: 21. Merge Two Sorted Lists

        head = sort_list = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val:
                sort_list.next = list1
                list1 = list1.next

            else:
                sort_list.next = list2
                list2 = list2.next
            sort_list = sort_list.next

        sort_list.next = list1 or list2
        return head.next


class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        heap = []

        for idx, el in enumerate(lists):
            if el:
                heapq.heappush(heap, (el.val, idx))

        while heap:
            val, idx = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next

            if lists[idx].next:
                lists[idx] = lists[idx].next
                heapq.heappush(heap, (lists[idx].val, idx))

        return dummy.next
