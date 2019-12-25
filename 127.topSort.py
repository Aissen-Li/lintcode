class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        from collections import deque
        if not graph:
            return []

        node_indegree = {i: 0 for i in graph}
        for node in graph:
            for neighbor in node.neighbors:
                node_indegree[neighbor] += 1

        res = []
        start_nodes = [i for i in graph if node_indegree[i] == 0]
        queue = deque(start_nodes)
        while queue:
            node = queue.popleft()
            res.append(node)
            for neighbor in node.neighbors:
                node_indegree[neighbor] -= 1
                if node_indegree[neighbor] == 0:
                    queue.append(neighbor)
        return res