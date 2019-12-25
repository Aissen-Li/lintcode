class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        if not node:
            return node
        root = UndirectedGraphNode(node.label)
        visited = {}
        visited[root.label] = root
        q = [node]
        while q:
            cur = q.pop()
            for n in cur.neighbors:
                if n.label not in visited:
                    visited[n.label] = UndirectedGraphNode(n.label)
                    q.append(n)
                visited[cur.label].neighbors.append(visited[n.label])
        return root
