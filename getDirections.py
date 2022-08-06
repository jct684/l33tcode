# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        #inorder search to find the start value and the destination value
        #save the direction relative to the root using a stack
        #compare root --> start and root --> destination and remove repeated values from root --> start
        #the remaining elements are U to create start --> X
        #compare root --> start and root --> destination and remove repeated values from root --> destination
        #append the remaining values to start --> X to create start --> destination
        #return the result as a string by using join function
        startValue_path = []
        destValue_path = []
        found_target = False
        startValue_path = self.root_to_target(root, startValue, startValue_path, found_target)[0]
        startValue_path.reverse()
        destValue_path = self.root_to_target(root, destValue, destValue_path, found_target)[0]
        destValue_path.reverse()
        i = 0
        while i < min(len(startValue_path), len(destValue_path)) and startValue_path[i] == destValue_path[i]:
            startValue_path.remove(startValue_path[i])
            destValue_path.remove(destValue_path[i])
        reversed_startValue_path = ["U" for item in startValue_path]
        reversed_startValue_path.extend(destValue_path)
        return "".join(reversed_startValue_path)
    
    def root_to_target(self, root, target, path, found_target):
        if root.val == target:
            found_target = True
            return [path, found_target]
        if root.left:
            res = self.root_to_target(root.left, target, path, found_target)
            path = res[0]
            found_target = res[1]
            if found_target:
                path.append("L")
                return [path, found_target]
        if root.right:
            res = self.root_to_target(root.right, target, path, found_target)
            path = res[0]
            found_target = res[1]
            if found_target:
                path.append("R")
                return [path, found_target]
        return [path, found_target]