# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        return recoverTree(root)

def recoverTree(root):
    #inorder DFS search provides an array in ascending order
    #when you find a value that doesn't belong, save the predecessor
    #search for smallest value that doesn't belong after the predecessor to swap with the predecessor
    #time complexity O(n)
    #space complexity O(n)
    swap_dict = {'first': None, 'second': None, 'predecessor':None}
    DFS_inorder(root, swap_dict)
    swap_dict['first'].val, swap_dict['second'].val = swap_dict['second'].val, swap_dict['first'].val

def DFS_inorder(root, swap_dict):
    if root  == None:
        return
    DFS_inorder(root.left, swap_dict)
    if swap_dict['predecessor'] is not None and root.val <  swap_dict['predecessor'].val:
        if swap_dict['first'] is None:
            swap_dict['first'] = swap_dict['predecessor']
        swap_dict['second'] = root
    swap_dict['predecessor'] = root
    DFS_inorder(root.right, swap_dict)