# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return BFSinvertTree(root)
        #return recursiveInvertTree(root)
        
        
def BFSinvertTree(root):
    if(root == None):
        return None
    dq = deque([root])
    while(dq):
        curr_node = dq.popleft()
        new_right = None
        new_left = None
        if(curr_node.left):
            dq.append(curr_node.left)
            new_right = curr_node.left
        if(curr_node.right):
            dq.append(curr_node.right)
            new_left = curr_node.right
        curr_node.left = new_left
        curr_node.right = new_right
    return root

def recursiveInvertTree(root):
    if(root == None):
        return None
    left = recursiveInvertTree(root.left)
    right = recursiveInvertTree(root.right)
    root.left = right
    root.right = left
    return root
            