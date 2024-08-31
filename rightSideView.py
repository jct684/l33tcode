# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #space complexity O(n)
        #time complexity O(n)
        if not root:
            return []
        level = 0
        dq = deque([(root, level)])
        tree_info = []
        max_level = 0
        while dq:
            node_info = dq.popleft()
            node = node_info[0]
            level = node_info[1]
            max_level = max(max_level, level)
            tree_info.append((node.val, level))
            if node.right:
                dq.append((node.right, level+1))
            if node.left:
                dq.append((node.left, level+1))
        res = []
        level_num = 0
        while level_num <= max_level:
            for val, level in tree_info:
                if level == level_num:
                    level_num += 1
                    res.append(val)
        return res