def deleteNode(self, node) -> None:
    node.val = node.next.val
    node.next = node.next.next
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    
    Input: head = [4,5,1,9], node = 5
    Output: [4,1,9]
    """
