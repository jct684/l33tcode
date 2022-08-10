# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        #track what level you are on to determine position in resulting array
        #time complexity O(n), check every node once and store in array based on level
        #space complexity O(n) where n is
        self.res = []
        self.DFS(root)
        return self.res
    
    def DFS(self, root, level=0):
        if not root:
            return level
        left = self.DFS(root.left, level)
        right = self.DFS(root.right, level)
        level = max(left, right)
        if level < len(self.res):
            self.res[level].append(root.val)
        else:
            self.res.append([root.val])
        return level + 1