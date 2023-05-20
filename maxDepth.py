# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #return BFSmaxDepth(root)
        return DFSmaxDepth(root)
        
def BFSmaxDepth(root):
    #time complexity O(n)
    #space complexity O(n)
    if root == None:
        return 0
    depth = 1
    dq = deque([(root, depth)])
    max_depth = 0
    while(dq):
        curr_node, depth = dq.popleft()
        max_depth = max(max_depth, depth)
        if curr_node.left:
            dq.append((curr_node.left, depth+1))
        if curr_node.right:
            dq.append((curr_node.right, depth+1))
    return max_depth

def DFSmaxDepth(node):
    #time complexity O(n)
    #space complexity O(n)
    if node == None:
        return 0
    left = DFSmaxDepth(node.left)
    right = DFSmaxDepth(node.right)
    return max(left, right) + 1
        
    
