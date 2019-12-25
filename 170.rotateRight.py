class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotateRight(self, head, k):
        if not head:
            return head
        p = head
        size = 1
        while p:
            p = p.next
            size += 1
        size -= 1
        k = k % size

        if k == 0:
            return head

        p = head
        count = 1
        while count < size - k:
            p = p.next
            count += 1
        newhead = p.next
        p.next = None
        p = newhead
        while p.next:
            p = p.next
        p.next = head
        return newhead