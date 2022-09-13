# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        #DFS search where the needs of coins at leaf nodes are passed up
        #the overall number of coins needed that are passed up can be saved in a pass by reference type such as dictionary or array or a global variable
        #time complexity O(n)
        #space complexity O(k) where kis the height of the tree
        return distributeCoins(root)

def distributeCoins(root):
    tracker = [0]
    DFS_postorder(root, tracker)
    return tracker[0]

def DFS_postorder(root, tracker):
    left = 0
    right = 0
    if root is None:
        return 0
    left = DFS_postorder(root.left, tracker)
    right = DFS_postorder(root.right, tracker)
    tracker[0] += abs(left) + abs(right)
    return root.val + left + right - 1