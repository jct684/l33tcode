# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        #DFS where you store the leaf nodes as found
        #a leaf node does not have children
        #time complexity O(n^2) I think because I have to delete leaves and search for new leaves repeatedly but somehow this is faster than 98% leetcode solutions so I'm not sure
        #space complexity O(n) spaced used by solution array
        DFS_saved = []
        self.parent_set = set()
        while root:
            DFS_leaf = []
            DFS_saved.append(self.DFS(root, DFS_leaf))
            for v in self.parent_set:
                if v[1] == "L":
                    v[0].left = None
                if v[1] == "R":
                    v[0].right = None
                if v[1] == "":
                    root = None
            self.parent_set.clear()
        return DFS_saved
            
    
    def DFS(self, root, DFS_leaf, direction= "", parent=""):
        if root.left:
            parent = root
            direction = "L"
            self.DFS(root.left, DFS_leaf, direction, parent)
        if root.right:
            parent = root
            direction = "R"
            self.DFS(root.right, DFS_leaf, direction, parent)
        if root.left == None and root.right == None:
            DFS_leaf.append(root.val)
            self.parent_set.add((parent, direction))
        return DFS_leaf
            
        
        