"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        ancestors = {}
        ancestors[q] = True
        ancestors[p] = True
        return lowest_common_ancestor(p, q, ancestors)

def lowest_common_ancestor(p, q, ancestors):
    #traverse up one target until reaching root
    #if the other target is found then ancestor is the other target
    #use a dictionary to store all the objects up to root as found
    #if the other target is not found, then start from other target and traverse up until finding a corresponding key in the dictionary
    #time complexity O(height of tree)
    #space complexity O(height of tree)
    current_node = p
    while current_node.parent:
        current_node = current_node.parent
        if ancestors.get(current_node, False):
            return current_node
        else:
            ancestors[current_node] = True
    current_node = q
    while current_node.parent:
        current_node = current_node.parent
        if ancestors.get(current_node, False):
            return current_node