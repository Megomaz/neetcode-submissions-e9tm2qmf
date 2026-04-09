# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # deleting a leaf node: no further actions
        # deleting node with 1 child: move up the node further
        # deleting node with 2 childs: move up right the node further
    

        def dfs(root,key):
            if not root:
                return None

            if key < root.val:
                root.left = dfs(root.left,key)
            elif key > root.val:
                root.right = dfs(root.right,key)
            else:
                if not root.left:
                    return root.right

                if not root.right:
                    return root.left
                

                successor = root.right
                while successor.left:
                    successor = successor.left
                root.val = successor.val

                root.right = dfs(root.right,successor.val)
            return root
        return dfs(root,key)
            
