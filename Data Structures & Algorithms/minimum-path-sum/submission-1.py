class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        rows,cols = len(grid), len(grid[0])

        def dfs(row,col):
            if row >= rows or col >= cols:
                return float('inf')
            
            if row == rows - 1 and col == cols - 1:
                return grid[row][col]   
            
            if (row,col) in dp:
                return dp[(row,col)]

            val = grid[row][col] + min(dfs(row + 1,col), dfs(row,col + 1))

            dp[(row,col)] = val
            return val

        return dfs(0,0)