class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


from collections import deque
class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('#')
        return res


    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    """
    def deserialize(self, data):
        data_TreeNode = []
        for i in data:
            if i != '#':
                data_TreeNode.append(TreeNode(i))
            else:
                data_TreeNode.append(None)
        parent, child = 0, 1
        while parent < len(data) and child < len(data):
            if data_TreeNode[parent]:
                data_TreeNode[parent].left = data_TreeNode[child]
                child += 1
                data_TreeNode[parent].right = data_TreeNode[child]
                child += 1
            parent += 1

        return data_TreeNode[0]

