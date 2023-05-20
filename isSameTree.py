# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #return BFSisSameTree(p, q)
        return DFSisSameTree(p, q)

def BFSisSameTree(p, q):
    #time complexity O(n)
    #space complexity O(n)
    dq1 = deque([p])
    dq2 = deque([q])
    while dq1 and dq2:
        node_p = dq1.popleft()
        node_q = dq2.popleft()
        if (node_p == None or node_q == None):
            if node_p != None or node_q != None:
                return False
        elif (node_p.val != node_q.val):
            return False
        if node_p != None:
            dq1.append(node_p.left)
            dq1.append(node_p.right)
        if node_q != None:
            dq2.append(node_q.left)
            dq2.append(node_q.right)
    if(len(dq1) != 0 or len(dq2) != 0):
        return False
    return True

def DFSisSameTree(p, q):
    #time complexity O(n)
    #space complexity O(n)
    if p == None or q == None:
        if p != None or q != None:
            return False
        return True
    if (p.val != q.val):
        return False
    return DFSisSameTree(p.left, q.left) and DFSisSameTree(p.right, q.right)