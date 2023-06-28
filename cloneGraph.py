"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #time complexity O(V+E)
        #space complexity O(V)
        if node == None:
            return None
        cloned = {}
        def dfs(node):
            if node in cloned:
                return cloned[node]
            copy_node = Node(node.val)
            cloned[node] = copy_node
            for neighbors in node.neighbors:
                copy_node.neighbors.append(dfs(neighbors))
            return copy_node
        return dfs(node)