class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        #inorder search to find the start value and the destination value
        #save the direction relative to the root using a stack
        #compare root --> start and root --> destination and remove repeated values from root --> start
        #the remaining elements are U to create start --> X
        #compare root --> start and root --> destination and remove repeated values from root --> destination
        #append the remaining values to start --> X to create start --> destination
        #return the result as a string by using join function
        #bool of "" and None is false while bool of characters and objects is True, can use this to improve recursive function by avoiding flag in previous version
        ancestor = self.lowest_common_ancestor(root, startValue, destValue)
        start_path = self.find_path(ancestor, startValue)
        end_path = self.find_path(ancestor, destValue)
        start_path_up = "U" * len(start_path)
        return "".join([start_path_up,end_path])
    
    def find_path(self, ancestor, target, path=[], direction=""):
        if ancestor is None:
            return ""
        if ancestor.val == target:
            path.append(direction)
            return "".join(path)
        path.append(direction)
        left = self.find_path(ancestor.left, target, path, "L")
        right = self.find_path(ancestor.right, target, path, "R")
        path.pop()
        return left or right
    
    def lowest_common_ancestor(self, root, first, second):
        if root is None:
            return ""
        if root.val == first or root.val == second:
            return root
        left = self.lowest_common_ancestor(root.left, first, second)
        right = self.lowest_common_ancestor(root.right, first, second)
        if left and right:
            return root
        return left or right