class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: ListNode head is the head of the linked list
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        curr = head

        for i in range(m - 1):
            pre = pre.next
            curr = curr.next

        pre_forzen = pre
        curr_forzen = curr
        pre = pre.next
        curr = curr.next

        for i in range(n - m):
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp

        pre_forzen.next = pre
        curr_forzen.next = curr

        return dummy.next