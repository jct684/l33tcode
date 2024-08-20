# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #time complexity O(n)
        #space complexity O(n)
        gap = 0
        
        def dfs(root):
            if not root:
                return 0
            left_level = dfs(root.left)
            right_level = dfs(root.right)
            nonlocal gap 
            gap = max(gap, abs(left_level - right_level))
            return max(left_level, right_level)+1
        
        if root:
            dfs(root)
        if gap > 1:
            return False
        return True