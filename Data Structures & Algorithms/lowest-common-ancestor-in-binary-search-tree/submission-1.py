# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(root):
            if not root:
                return root
            
            # not both on same path
            # we encounter any of them

            if (p.val > root.val and q.val < root.val) or (p.val < root.val and q.val > root.val):
                return root
            elif root.val == p.val:
                return p
            elif root.val == q.val:
                return q
            else:
                if root.val > p.val:
                    return dfs(root.left)
                else:
                    return dfs(root.right)

        return dfs(root)