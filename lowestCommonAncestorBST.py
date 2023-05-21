# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #time complexity O(n), average O(log n)
        #space complexity O(1)
        ancestor_node = root
        high = 0
        low = 0
        if (p.val > q.val):
            low = q.val
            high = p.val
        else:
            low = p.val
            high = q.val
        while((ancestor_node.val < low) or (ancestor_node.val > high)):
            if(ancestor_node.val < low):
                ancestor_node = ancestor_node.right
            elif(ancestor_node.val > high):
                ancestor_node = ancestor_node.left
        return ancestor_node