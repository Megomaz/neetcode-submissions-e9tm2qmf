# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        q = deque([root])
        idx = 0

        while q:
            size = len(q)

            for _ in range(size):
                root = q.popleft()

                if not root:
                    continue
                
                if len(res) == idx:
                    res.append(root.val)
                else:
                    res[idx] = root.val
                
                if root.left:
                    q.append(root.left)
                
                if root.right:
                    q.append(root.right)
            idx += 1
        return res