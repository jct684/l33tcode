# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def DFSpreorder(root):
            if root != None:
                res.append(str(root.val))
                DFSpreorder(root.left)
                DFSpreorder(root.right)
            else:
                res.append("N")
        DFSpreorder(root)
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        res = data.split(",")
        dq = deque(res)
        def undoDFSpreorder(dq):
            if(dq[0] == 'N'):
                dq.popleft()
                return None
            node_val = dq.popleft()
            node = TreeNode(node_val)
            node.left = undoDFSpreorder(dq)
            node.right = undoDFSpreorder(dq)
            return node
        return undoDFSpreorder(dq)
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))