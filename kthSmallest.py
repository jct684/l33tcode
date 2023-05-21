# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #time complexity O(n)
        #space complexity O(n)
        inorder_arr = []
        DFSinorder(root, k, inorder_arr)
        return inorder_arr[k-1]

def DFSinorder(root, k, inorder_arr):
    if root == None:
        return None
    if(len(inorder_arr) >= k): #Note: this will overshoot because of how the stack works but slightly more efficient
        return
    DFSinorder(root.left, k, inorder_arr)
    inorder_arr.append(root.val)
    DFSinorder(root.right, k, inorder_arr)