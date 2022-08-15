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
        root = p
        while root.parent:
            root = root.parent
            if root.val == q.val:
                return root
        return lowest_common_ancestor(root, p, q)

def lowest_common_ancestor(root, p, q):
    #DFS to find the targets p and q
    #return nothing or return the node if it the target
    #when a node receives a node from both left and right children then it is the lowest common ancestor
    #when a node receives a node from one side, it needs to pass up that node
    #time complexity O(n)
    #space complexity O(n)
    #there is probably a faster way with O(height of tree) time complexity where we only go up instead of going back down the tree 
    if root is None:
        return ""
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    if left or right:
        if root.val == p.val:
            return root
        return left or right
    if root.val == p.val or root.val == q.val:
        return root
    return ""
    
    
    
    
        