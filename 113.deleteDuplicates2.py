class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of the linked list
    """
    def deleteDuplicates(self, head):
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        curr = head
        pre = dummy

        while curr.next:
            if curr.val != curr.next.val:
                pre.next = curr
                curr = curr.next
                pre = pre.next

            else:
                while curr and curr.next.val == curr.val:
                    curr = curr.next
                if not curr:
                    pre.next = None
                    break

        return dummy.next

