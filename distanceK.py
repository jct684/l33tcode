# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        #dictionary to store ancestors as you look for node using DFS
        #Once you find the node, perform BFS from the node including distance
        #Traverse down children and up ancestors until distance is reached
        #time complexity O(n)
        #space complexity O(n)
        return distanceK(root, target, k)

def distanceK(root, target, k):
    ancestor_dict = {}
    visited = {}
    left = None
    right = None
    BFS_root = DFS(root, target, ancestor_dict, left, right)
    return BFS(BFS_root, k, ancestor_dict, visited)
    

def DFS(root, target, ancestor_dict, left, right):
    if root == target:
        return root
    if root.left:
        ancestor_dict[root.left] =  root
        left = DFS(root.left, target, ancestor_dict, left, right)
    if root.right:
        ancestor_dict[root.right] = root
        right = DFS(root.right, target, ancestor_dict, left, right)
    if root.left is False and root.right is False:
        return []
    return left or right
    
    
def BFS(BFS_root, k, ancestor_dict, visited):
    q = deque()
    q.append((BFS_root, 0))
    distance = 0
    ans = []
    while len(q) > 0:
        root, distance = q.popleft()
        visited[root] = True
        if distance == k:
            ans.append(root.val)
        else:
            if root.left and visited.get(root.left, False) is not True:
                q.append((root.left, distance+1))
            if root.right and visited.get(root.right, False) is not True:
                q.append((root.right, distance+1))
            if ancestor_dict.get(root, False) and visited.get(ancestor_dict[root], False) is not True:
                q.append((ancestor_dict[root], distance +1))
    return ans