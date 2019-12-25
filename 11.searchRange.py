class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


from collections import deque


class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        if not root:
            return []
        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if k1 <= node.val <= k2:
                result.append(node.val)
            if node.left and node.val >= k1:
                queue.append(node.left)
            if node.right and node.val <= k2:
                queue.append(node.right)
        return sorted(result)


node1 = TreeNode(20)
node2 = TreeNode(1)
node3 = TreeNode(40)
node4 = TreeNode(35)
node1.left = node2
node1.right = node3
node3.left = node4
test = Solution()
print(test.searchRange(node1, 1, 37))