"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        def findroot(node):
            while node.parent:
                node = node.parent
            return node
        
        def dfs(root):
            if not root:
                return None
            
            if root == p or root == q:
                return root
            
            left = dfs(root.left)
            right = dfs(root.right)

            if left and right:
                return root
            
            if left:
                return left
            return right

        return dfs(findroot(p))
        #def dfs(root):