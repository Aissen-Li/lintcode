class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of linked list
    """
    def deleteDuplicates(self, head):
        res = ListNode(0)
        res.next = head
        temp = res.next
        while temp:
            if not temp.next:
                break
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return res.next