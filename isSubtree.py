# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #DFS is easier than BFS
        #time complexity O(n*m)
        #space complexity O(n+m)
        if(root == None):
            return False
        if(DFSisSameTree(root, subRoot)):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
def DFSisSameTree(p, q):
    if p == None or q == None:
        if p != None or q != None:
            return False
        return True
    if (p.val != q.val):
        return False
    return DFSisSameTree(p.left, q.left) and DFSisSameTree(p.right, q.right)