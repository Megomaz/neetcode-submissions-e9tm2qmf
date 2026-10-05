from collections import deque
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        rows, cols = len(grid), len(grid[0])
        dp = [[float('inf')] * cols for _ in range(rows)]
        
        heap = [(grid[0][0], 0,0)]
        dp[0][0] = grid[0][0]
        
        while heap:
            val,row,col = heapq.heappop(heap)
            
            if val > dp[row][col]:
                continue

            for dr, dc in directions:
                nr,nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    v = max(val, grid[nr][nc])
                    if v < dp[nr][nc]: 
                        dp[nr][nc] = v
                        heapq.heappush(heap,(v, nr,nc))

        return dp[rows-1][cols-1]

    