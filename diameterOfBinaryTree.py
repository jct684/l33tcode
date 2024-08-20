# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #time complexity O(n)
        #space complexity O(n)
        
        def dfs(root):
            if not root:
                return 0
            level_left = dfs(root.left) 
            level_right = dfs(root.right)
            nonlocal diameter
            diameter = max(diameter, level_left+level_right)
            return max(level_left, level_right)+1
        
        diameter = 0
        if root:
            dfs(root)

        return diameter