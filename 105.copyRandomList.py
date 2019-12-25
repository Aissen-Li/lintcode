class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        if not head:
            return head

        relation = {}
        curr = head
        while curr:
            relation[curr] = RandomListNode(curr.label)
            curr = curr.next

        curr = head
        while curr:
            if curr.next:
                relation[curr].next = relation[curr.next]
            if curr.random:
                relation[curr].random = relation[curr.random]
            curr = curr.next

        return relation[head]