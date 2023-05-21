# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #time complexity O(n)
        #space complexity O(n)
        if(root == None):
            return None
        ans = []
        dq = deque([(root, 0)])
        curr_level = 0
        level_arr = []
        while dq:
            root, level = dq.popleft()
            if(level != curr_level):
                curr_level = level
                ans.append(level_arr)
                level_arr = []
            level_arr.append(root.val)
            if(root.left):
                dq.append((root.left, level+1))
            if(root.right):
                dq.append((root.right, level+1))
        ans.append(level_arr)
        return ans