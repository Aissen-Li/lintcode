class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        res1 = ListNode(0)
        res2 = ListNode(0)
        temp1 = res1
        temp2 = res2
        while head:
            if head.val < x:
                temp1.next = head
                temp1 = temp1.next
            else:
                temp2.next = head
                temp2 = temp2.next
            head = head.next
        temp1.next = res2.next
        temp2.next = None
        return res1.next