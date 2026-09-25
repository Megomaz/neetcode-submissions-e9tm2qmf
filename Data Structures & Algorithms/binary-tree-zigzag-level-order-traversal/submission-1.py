# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = deque([root])
        left = True

        while q:
            size = len(q)
            curr = []
            for _ in range(size):
                root = q.popleft()
               
                if not root:
                    continue
                curr.append(root.val)

                if root.left:
                    q.append(root.left)

                if root.right:
                    q.append(root.right)

            
            if curr:
                if left:
                    res.append(curr)
                else:
                    res.append(curr[::-1])
                left = not(left)
        return res