class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows,cols = len(obstacleGrid), len(obstacleGrid[0])
        cache = {}
        def dfs(row,col):
            if row == rows or col == cols:
                return 0

            if obstacleGrid[row][col] == 1:
                return 0

            if row == rows - 1 and col == cols -1:
                return 1

            if (row,col) in cache:
                return cache[(row,col)]

            val = 0

            val += dfs(row + 1, col)  + dfs(row, col + 1)
            cache[(row,col)] = val
            return val

        return dfs(0,0)
