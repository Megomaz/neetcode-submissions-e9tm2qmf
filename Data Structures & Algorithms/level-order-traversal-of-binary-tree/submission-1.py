# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = deque([root])

        while q:
            size = len(q)
            arr = []

            for _ in range(size):
                root = q.popleft()

                if not root:
                    continue

                arr.append(root.val)

                if root.left:
                    q.append(root.left)
                
                if root.right:
                    q.append(root.right)
            if arr:
                res.append(arr)
        return res
