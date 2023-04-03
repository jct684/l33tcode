# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder_arr = []
        inOrder(root, inorder_arr)
        for i in range(1, len(inorder_arr)):
            if inorder_arr[i] <= inorder_arr[i-1]:
                return False
        return True

def inOrder(root, inorder_arr):
    if root != None:
        inOrder(root.left, inorder_arr)
        inorder_arr.append(root.val)
        inOrder(root.right, inorder_arr)