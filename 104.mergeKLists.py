
class ListNode(object):
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        import sys
        k = len(lists)
        listValue = [0] * k
        for i in range(k):
            if lists[i] is not None:
                listValue[i] = lists[i].val
            else:
                listValue[i] = sys.maxsize
        res = ListNode(0)
        currentPos = res
        while listValue != [sys.maxsize] * k:
            minValue = min(listValue)
            minIndex = listValue.index(minValue)
            currentPos.next = ListNode(minValue)
            if not lists[minIndex].next:
                listValue[minIndex] = sys.maxsize
            else:
                listValue[minIndex] = lists[minIndex].next.val
            print(listValue)
        currentPos.next = None
        return res.next

test1 = ListNode(2, ListNode(4, ListNode(5)))
test2 = None
test3 = ListNode(-1, ListNode(1))
s = Solution()
print(s.mergeKLists([test1, test2, test3]))

import heapq

# overwrite the compare function
# so that we can directly put ListNode into heapq
ListNode.__lt__ = lambda x, y: (x.val < y.val)


class Solution2:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        if not lists:
            return None

        dummy = ListNode(0)
        tail = dummy
        heap = []
        for head in lists:
            if head:
                heapq.heappush(heap, head)

        while heap:
            head = heapq.heappop(heap)
            tail.next = head
            tail = head
            if head.next:
                heapq.heappush(heap, head.next)

        return dummy.next
