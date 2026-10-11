# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def serialize(root):
            if not root:
                return '#'
            
            s = ','.join([str(root.val), serialize(root.left), serialize(root.right)])
            return s
        
        r1 = serialize(root)
        r2 = serialize(subRoot)

        return r2 in r1