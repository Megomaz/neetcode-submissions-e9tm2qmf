# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, leftRange, rightRange):
            if not root:
                return True
            
            if not leftRange < root.val < rightRange:
                return False
            
            return dfs(root.left,leftRange , root.val) and dfs(root.right,root.val , rightRange)
        
        return dfs(root, -float('inf'), float('inf'))