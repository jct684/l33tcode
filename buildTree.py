# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #time complexity O(n)
        #space complexity O(n)
        if(len(preorder) == 0 or len(inorder) == 0):
            return None
        new_node = TreeNode()
        new_node.val = preorder[0]
        split_index = inorder.index(new_node.val)
        new_node.left = self.buildTree(preorder[1:split_index+1], inorder[:split_index])
        new_node.right = self.buildTree(preorder[split_index+1:], inorder[split_index+1:])
        return new_node