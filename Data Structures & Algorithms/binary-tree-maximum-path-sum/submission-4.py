# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -float('inf')

        def dfs(root):
            if not root:
                return -float('inf')
            
            left = dfs(root.left)
            right = dfs(root.right)

            val = root.val

            max_path = max(val, val + left, val + right)
            self.res = max(self.res, val + left + right,max_path)
            return max_path

        dfs(root)
        return self.res