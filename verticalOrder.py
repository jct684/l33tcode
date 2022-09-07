import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #BFS
        #record the traversal from the root as left -= 1 and right += 1
        #save the vertical level and normalize the most negative value as index 0 of the output array
        #maybe use a dictionary to save the level and generate the output array at the end
        #time complexity O(n)
        #space complexity O(n)
        return verticalOrder(root)

def verticalOrder(root):
    if root is None:
        return []
    
    vertical_level = 0
    index_dict = collections.defaultdict(list)
    first_index = 0
    last_index = 0
    q = collections.deque()
    q.append((root, vertical_level))
    while len(q) > 0:
        current, vertical_level = q.popleft()
        index_dict[vertical_level].append(current.val)
        if current.left:
            q.append((current.left, vertical_level-1))
            first_index = min(first_index, vertical_level-1)
        if current.right:
            q.append((current.right, vertical_level+1))
            last_index = max(last_index, vertical_level+1)
    return [index_dict[index] for index in range(first_index, last_index+1)]