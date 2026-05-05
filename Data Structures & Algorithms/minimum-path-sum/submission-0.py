class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cache = {}
        rows,cols = len(grid), len(grid[0])

        def dfs(row,col):
            if not 0 <= row < rows or not 0 <= col < cols:
                return float('inf')
            
            if row == rows -1 and col == cols -1:
                return grid[row][col]

            if (row,col) in cache:
                return cache[(row,col)]
            
            val = grid[row][col]

            val += min(dfs(row + 1,col), dfs(row,col + 1))

            cache[(row,col)] = val
            return val

        return dfs(0,0)