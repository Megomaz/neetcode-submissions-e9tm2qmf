# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        def dfs(root, maxVal):
            if not root:
                return 0
            
            v = 1 if root.val >= maxVal else 0

            left = dfs(root.left, max(root.val, maxVal))
            right = dfs(root.right, max(root.val, maxVal))

            return v + left + right
        
        return dfs(root, -float('inf'))