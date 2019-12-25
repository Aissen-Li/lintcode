class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        res = self.dfs(head)
        return res

    def dfs(self, head):
        if not head:
            return head
        if not head.next:
            return TreeNode(head.val)

        dummy = ListNode(0)
        dummy.next = head
        fast = dummy.next
        slow = dummy

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None
        parent = TreeNode(mid.val)

        parent.left = self.dfs(head)
        parent.right = self.dfs(mid.next)

        return parent
