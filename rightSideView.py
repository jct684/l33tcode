# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #preorder search along right side instead of typical left side
        #track the level and if the level does not exist then add root.val
        #if the level does exist, continue traversal
        #time complexity O(n)
        #space complexity O(n)
        #this one seems like an easy problem
        return rightSideView(root)

def rightSideView(root):
    if root:
        ans = []
        dict_level = {}
        level = 0
        return DFS(root, ans, dict_level, level)
    return []

def DFS(root, ans, dict_level, level):
    if dict_level.get(level, False) is False:
        ans.append(root.val)
        dict_level[level] = True
    level += 1
    if root.right:
        DFS(root.right, ans, dict_level, level)
    if root.left:
        DFS(root.left, ans, dict_level, level)
    return ans