class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The head of linked list.
    @return: nothing
    """
    def reorderList(self, head):
        if not head or not head.next:
            return head

        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None

        pre = None
        curr = mid
        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp

        cur1, cur2 = head, pre
        while cur2:
            next1, next2 = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = next1
            cur1, cur2 = next1, next2

        return head
