class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, value):
        parent = None
        node = root
        while node and node.val != value:
            parent = node
            if node.val > value:
                node = node.left
            else:
                node = node.right

        if not node:
            return root

        elif not node.left and not node.right:
            if parent:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
                return root
            return None

        elif node.left and node.right:
            pre_parent = node
            pre = node.left
            while pre.right:
                pre_parent = pre
                pre = pre.right
            if pre_parent != node:
                pre_parent.right = pre.left
                node.val = pre.val
            else:
                node.val = pre.val
                node.left = pre.left
            return root

        else:
            if parent:
                if parent.left == node:
                    parent.left = node.left or node.right
                else:
                    parent.right = node.left or node.right
                return root
            else:
                return node.left or node.right
