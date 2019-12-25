class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        rootpos = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: rootpos+1], inorder[:rootpos])
        root.right = self.buildTree(preorder[rootpos+1:], inorder[rootpos+1:])
        return root