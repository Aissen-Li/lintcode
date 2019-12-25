class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        if not head:
            return None
        if not head.next:
            return head

        p = head
        pre = None
        while p:
            temp = p.next
            p.next = pre
            pre = p
            p = temp
        return pre
