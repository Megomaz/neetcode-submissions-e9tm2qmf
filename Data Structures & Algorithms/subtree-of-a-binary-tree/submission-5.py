# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(root,subRoot):
            if not root and not subRoot:
                return True
            
            if not root or not subRoot:
                return False
            
            if root.val != subRoot.val:
                return False
            
            left = helper(root.left,subRoot.left)
            right = helper(root.right,subRoot.right)

            return left and right

        def dfs(root,subRoot):
            if not root or not subRoot:
                return False
            v = False
            if root.val == subRoot.val:
                v = helper(root, subRoot)
            
            left = dfs(root.left,subRoot)
            right = dfs(root.right,subRoot)

            return v or left or right

        return dfs(root,subRoot)