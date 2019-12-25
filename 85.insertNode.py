class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        if not root:
            return node

        p = root
        while p:
            if p.val >= node.val:
                if not p.left:
                    break
                p = p.left
            else:
                if not p.right:
                    break
                p = p.right

        if p.val >= node.val:
            p.left = node
        else:
            p.right = node
        return root
