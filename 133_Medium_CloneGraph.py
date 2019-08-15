"""
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        graph = {}
        processed = set()
        queue = deque([node])
        head = None
        while len(queue) > 0:
            node = queue.popleft()

            if node in processed:
                continue
            if node in graph:
                new_node = graph[node]
            else:
                new_node = Node(node.val, [])
                graph[node] = new_node
            for neighbor in node.neighbors:
                if neighbor in graph:
                    new_node.neighbors.append(graph[neighbor])
                else:
                    new_neigh = Node(neighbor.val, [])
                    graph[neighbor] = new_neigh
                    new_node.neighbors.append(new_neigh)
                queue.append(neighbor)
            processed.add(node)
            if not head:
                head = new_node
        return head

