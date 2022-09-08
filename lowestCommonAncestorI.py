# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #return your own node if target
        #if two nodes are found then return return current node as the lca
        #time compelxity O(n)
        #space complexity O(1)
        #cases: current node target and receive a bubbled up node = current node is lca
        #       two different nodes bubled up = current node is lca
        # DFS search
        return lowestCommonAncestor(root, p, q)

def lowestCommonAncestor(root, p, q):
    return DFS(root, p, q)

def DFS(root, p, q):
    if root is None:
        return None
    if root == p or root == q:
        return root
    left = DFS(root.left, p, q)
    right = DFS(root.right, p, q)
    if left and right:
        return root
    if left or right:
        return left or right
    return None