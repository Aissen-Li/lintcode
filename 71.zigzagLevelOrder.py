class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

from collections import deque
class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        queue = deque([root])
        level = 0
        res = []
        while queue:
            next_queue = deque([])
            temp = []
            for i in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            print(temp)
            if level % 2 == 0:
                res.append(temp)
            else:
                res.append(temp[::-1])
            level += 1
            queue = next_queue
        return res


test = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3
print(test.zigzagLevelOrder(node1))