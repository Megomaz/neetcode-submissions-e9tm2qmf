# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        def dfs(root):
            if not root:
                return '#'
            
            s = ','.join([str(root.val),dfs(root.left), dfs(root.right)])
            return s
        return dfs(root)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        idx = 0
        data = data.split(',')

        def dfs():
            nonlocal idx

            if data[idx] == '#':
                idx += 1
                return 
            
            node = TreeNode(int(data[idx]))
            idx += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()