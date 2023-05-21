# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #inorder_arr = []
        #DFSinorder(root, k, inorder_arr)
        #return inorder_arr[k-1]
        return iterativeInorder(root, k)

def DFSinorder(root, k, inorder_arr):
    #time complexity O(n)
    #space complexity O(n)
    if root == None:
        return None
    if(len(inorder_arr) >= k): #Note: this will overshoot because of how the stack works but slightly more efficient
        return
    DFSinorder(root.left, k, inorder_arr)
    inorder_arr.append(root.val)
    DFSinorder(root.right, k, inorder_arr)

def iterativeInorder(root, k):
    #time complexity O(n)
    #space complexity O(k) where k is height of tree
    dq = deque()
    curr_node = root
    count = 0
    while True:
        while(curr_node):
            dq.append(curr_node)
            curr_node = curr_node.left
        curr_node = dq.pop()
        count += 1
        if (count == k):
            return curr_node.val
        curr_node = curr_node.right