# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}

        def dfs(root):
            if not root:
                return [0,0] # rob this node, skip this node

            leftRob, leftSkip = dfs(root.left)
            rightRob, rightSkip = dfs(root.right)

            rob_this_node = root.val + leftSkip + rightSkip
            skip_this_node = max(leftSkip,leftRob) + max(rightSkip,rightRob)

            return [rob_this_node,skip_this_node]
        
        return max(dfs(root))


            


            
