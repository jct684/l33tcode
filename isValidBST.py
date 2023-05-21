# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #time complexity O(n)
        #space complexity O(n)
        left = float('-inf')
        right = float('+inf')
        return DFS(root, left, right)
    
def DFS(node, left, right):
    if(node == None):
        return True
    if(node.val <= left or node.val >= right):
        return False
    left = DFS(node.left, left, node.val)
    right = DFS(node.right, node.val, right)
    return left and right