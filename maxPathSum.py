# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #time complexity O(n)
        #space complexity O(n)
        max_sum = root.val
        def DFS(root):
            nonlocal max_sum
            if(root == None):
                return 0
            left = max(DFS(root.left), 0)
            right = max(DFS(root.right), 0)
            max_sum = max(max_sum, root.val + left + right)
            return max(root.val + left, root.val + right)
        DFS(root)
        return max_sum