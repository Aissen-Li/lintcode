class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        if not root:
            return 0

        stack = []
        result = []
        depth = 0
        node = root

        while root or len(stack):
            while node:
                result.append(depth + 1)
                depth += 1
                stack.append([node, depth])
                node = node.left

            popnode = stack.pop()
            node = popnode[0]
            depth = popnode[1]
            node = node.right

        return max(result)
