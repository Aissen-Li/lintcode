class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):
    #     if not head or not head.next:
    #         return head
    #
    #     fast = head
    #     slow = head
    #     while fast and fast.next:
    #         pre = slow
    #         fast = fast.next.next
    #         slow = slow.next
    #     pre.next = None
    #     return self.merge(self.sortList(head), self.sortList(slow))
    #
    # def merge(self, l1, l2):
    #     if not l1:
    #         return l2
    #     if not l2:
    #         return l1
    #     if l1.val <= l2.val:
    #         l1.next = self.merge(l1.next, l2)
    #         return l1
    #     else:
    #         l2.next = self.merge(l1, l2.next)
    #         return l2

        if not head or not head.next:
            return head

        pivot = head
        l1 = ListNode(0)
        l2 = ListNode(0)
        equal = head
        small = l1
        large = l2
        temp = head.next
        while temp:
            if temp.val < pivot.val:
                small.next = temp
                small = small.next
            elif temp.val == pivot.val:
                equal.next = temp
                equal = equal.next
            else:
                large.next = temp
                large = large.next
            temp = temp.next

        small.next, equal.next, large.next = None, None, None

        l3 = self.sortList(l1)
        l4 = self.sortList(l2)
        if l3:
            p = l3
            while p.next:
                p = p.next
            p.next = pivot
            equal.next = l4
            return l3
        else:
            equal.next = l4
        return pivot

