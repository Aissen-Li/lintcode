class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2
    """
    def addLists(self, l1, l2):
        res = ListNode(0)
        p = res
        carry = 0

        while l1 or l2 or carry:
            num = 0
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
            num += carry
            digit, carry = num % 10, num // 10
            node = ListNode(digit)
            p.next = node
            p = p.next

        return res.next
