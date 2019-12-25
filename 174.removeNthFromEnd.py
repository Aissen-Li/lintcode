class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        res = ListNode(0)
        res.next = head
        temp = res
        for i in range(n):
            head = head.next
        while head:
            head = head.next
            temp = temp.next
        temp.next = temp.next.next
        return res.next